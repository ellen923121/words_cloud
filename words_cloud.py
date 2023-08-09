# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:35:28 2023

@author: student
"""

import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter



hotel_comments_ori = pd.read_csv('./agoda_comments_分詞_文字雲0724.csv', sep = ",", encoding = "UTF-8")
def wordscloud_nationality(nationality=None):
    
    try:
        
        if nationality is None or nationality == "":
            # 顯示所有縣市的文字雲
            df = hotel_comments_ori
        
        else:
            # 顯示指定縣市和鄉鎮的文字雲
            df = hotel_comments_ori[hotel_comments_ori['評論者國籍'] == nationality].reset_index(drop=True)
        
        all_comments_key_word = []
        for i in range(len(df)):
            tmp = eval(df['綜合評論_cut'][i])
            all_comments_key_word.extend(tmp)
            
        
        # 將所有分詞合成一個list
        all_comments_wordcloud = [word for word in all_comments_key_word if (len(word) >= 2) and (word != '酒店') and (word != '工作') and (word != '不錯')]
        # 合併成一個文本
        text = ' '.join(all_comments_wordcloud)
        
        #計算字頻
        #word_counts = Counter(all_comments_wordcloud)
        
        house_image= Image.open('./data/mask/house6.jpg')
        mask = np.array(house_image)
        
        wc = WordCloud(
            font_path='./fonts/NotoSansTC-Regular.otf',
            background_color='white', 
            mask=mask,
            width=1000,
            height=600,
            random_state=42,
        )
        
        # 生成詞雲 (wc.generate 用於純文字)
        wc.generate(str(text))

        # 生成詞雲 (wc.generate_from_frequencies 用於字頻)
        #wc.generate_from_frequencies(word_counts)
        
        
        # 顯示文字雲
        plt.figure(figsize=(12.0, 8.0), dpi=100)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()
     
    except:
        
        print("輸入錯誤，請重新輸入")

def wordscloud_city(city=None,town=None):
    
    try:
        
        if city is None or city == "":
            # 顯示所有縣市的文字雲
            df = hotel_comments_ori
        elif town is None or town == "":
            # 顯示指定縣市的文字雲
            df = hotel_comments_ori[hotel_comments_ori['縣市'] == city].reset_index(drop=True)
        else:
            # 顯示指定縣市和鄉鎮的文字雲
            df = hotel_comments_ori[(hotel_comments_ori['縣市'] == city) & (hotel_comments_ori['鄉鎮'] == town)].reset_index(drop=True)
        
        all_comments_key_word = []
        for i in range(len(df)):
            tmp = eval(df['綜合評論_cut'][i])
            all_comments_key_word.extend(tmp)
        
        # 將所有分詞合成一個list
        all_comments_wordcloud = [word for word in all_comments_key_word if (len(word) >= 2) and (word != '不錯') ]
        # 合併成一個文本
        text = ' '.join(all_comments_wordcloud)

        #計算字頻
        #word_counts = Counter(all_comments_wordcloud)
        
        house_image= Image.open('./data/mask/house6.jpg')
        mask = np.array(house_image)
        
        wc = WordCloud(
            font_path='./fonts/NotoSansTC-Regular.otf',
            background_color='white', 
            mask=mask,
            width=1000,
            height=600,
            random_state=42, 
        )
        
        # 生成詞雲 (wc.generate 用於純文字)
        wc.generate(str(text))

        # 生成詞雲 (wc.generate_from_frequencies 用於字頻)
        #wc.generate_from_frequencies(word_counts)
        
        # 顯示文字雲
        plt.figure(figsize=(12.0, 8.0), dpi=100)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()
     
    except:
        
        print("輸入錯誤，請重新輸入")



if __name__=='__main__':
    
    
    
    while True:
    
        nationality = input("請問你想看哪個國家遊客飯店評論文字雲 ?")
        if not nationality :
            pass
            
        else:
            wordscloud_nationality(nationality)
            print(f'這是{nationality}遊客的飯店評論文字雲')
            
        city = input("請問你想看哪個城市飯店評論文字雲 ?")   
        if not city:
            pass
        
        else:
            
            town = input("請問你想看哪個鄉鎮飯店評論文字雲? (如不須分鄉鎮，請直接按Enter)")
            wordscloud_city(city,town)
            print(f"這是{city}{town}的飯店文字雲")
        

    