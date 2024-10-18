syouhin = int(input("商品の金額："))
iretaokane = int(input("入れる金額："))
otsuri = syouhin - iretaokane
otsuri500 = 0
otsuri100 = 0
otsuri50 = 0
otsuri10 = 0
while otsuri > 10:
    if otsuri >= 500:   #おつりに500円玉が1枚以上含まれる場合
        otsuri500 += 1
        otsuri -= 500
    elif otsuri >= 100: #おつりに100円玉が1枚以上含まれる場合
        otsuri100 += 1
        otsuri -= 100
    elif otsuri >= 50:  #おつりに50円玉が1枚以上含まれる場合
        otsuri50 += 1
        otsuri -= 50
    elif otsuri >= 10:  #おつりに10円玉が1枚以上含まれる場合
        otsuri10 += 1
        otsuri -= 10
    else:   #ちょうどだった場合
        print("500円玉；",otsuri500,"枚")
        print("100円玉",otsuri100,"枚")
        print("50円玉",otsuri50,"枚")
        print("10円玉",otsuri10,"枚")
        break

#おつりの枚数表示
print("500円玉；",otsuri500,"枚")
print("100円玉",otsuri100,"枚")
print("50円玉",otsuri50,"枚")
print("10円玉",otsuri10,"枚")
