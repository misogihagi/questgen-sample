import nltk
import nltk.data
nltk.download('all')
from pprint import pprint
from Questgen import main
import requests
import random

YOUR_API_KEY = 'ここはご自分で発行されたKEYを入れてください'

def deepL_trans_to_en(text):

  # URLクエリに仕込むパラメータの辞書を作っておく
  params = {
              "auth_key": YOUR_API_KEY,
              "text": text,
              "source_lang": 'JA', # 入力テキストの言語を日本語に設定
              "target_lang": 'EN'  # 出力テキストの言語を英語に設定
          }
  # パラメータと一緒にPOSTする
  request = requests.post("https://api-free.deepl.com/v2/translate", data=params)

  result = request.json()
  return result["translations"][0]["text"]

def deepL_trans_to_ja(text):

  # URLクエリに仕込むパラメータの辞書を作っておく
  params = {
              "auth_key": YOUR_API_KEY,
              "text": text,
              "source_lang": 'EN', # 入力テキストの言語を英語に設定
              "target_lang": 'JA'  # 出力テキストの言語を日本語に設定
          }
  # パラメータと一緒にPOSTする
  request = requests.post("https://api-free.deepl.com/v2/translate", data=params)

  result = request.json()
  return result["translations"][0]["text"]

def prettyprint(text,output):
  # 問題文を取得
  Boolean_Questions = output["Boolean Questions"]

  Boolean_Questions_ja = [] # 問題文（日本語版）を格納
  for question in Boolean_Questions:
    Boolean_Questions_ja.append(deepL_trans_to_ja(question))

  print("【入力文】")
  print(text)
  print()

  for i in range(len(Boolean_Questions_ja)):
    print("【問題{}】".format(i+1))
    print(Boolean_Questions_ja[i])
    print()

def generate(ja_text):
  qe= main.BoolQGen() 
  en_text = deepL_trans_to_en(ja_text) # 日本語を英語に変換
  payload = {
            "input_text": en_text
        }
  output = qe.predict_boolq(payload) # 質問生成