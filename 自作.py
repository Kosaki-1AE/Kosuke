y = int(input('何年が知りたい？:'))
m = int(input('何月が知りたい？:'))
d = int(input('何日が知りたい？:'))
i=0
x=0
p=0
if y < 2000:
    i += 1
if m <= 3:
    o = int((y-1)%100)
else:
    o = int(y%100)
n = int(o/4) 
if y%4==0 and y%100==0 and y%400==0:
    if m==2:
        if d>=30:
            x+=3
        else:
            x+=2
else:
    if m==2:
        if d>=30:
            x+=3
    elif m==4 or m==6 or m==9 or m==11:
        if d>=31:
            x+=3
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d>=32:
            x+=3
    else:
        x+=3
num = [1,4,3,6,1,4,6,2,5,0,3,5]
if 1<=m<=12:
    day = num[m-1]
else:
    x+=3
if x >= 3:
    print('存在しない日です')
elif x==2:
    cipher = (o+n+day+d+i)%7
    day1 = ['土','日','月','火','水','木','金']
    day2 = day1[cipher]
    sign = ['牡羊座','牡牛座','双子座','蟹（かに）座','獅子座','乙女座','天秤座','蠍（サソリ）座','射手座','山羊座','水瓶座','魚（うお）座']
    for d in range(19,29):
        if day==2:
            signs = sign[11]
    for d in range(18):
        if day==3:
            signs = sign[11]
    for d in range(20,):
        if day==4:
            signs = sign[1]
        elif day==9:
            signs = sign[6]
        elif day==1:
            signs = sign[10]
    for d in range(19):
        if day==5:
            signs = sign[1]
        elif day==10:
            signs = sign[6]    
        elif day==2:
            signs = sign[10]
    for d in range(21,):
        if day==3:
            signs = sign[0]
        elif day==5:
            signs = sign[2]
    for d in range(20):
        if day==4:
            signs = sign[0]
        elif day==6:
            signs = sign[2]
    for d in range(22,):
        if day==6:
            signs = sign[3]
        elif day==12:
            signs = sign[9]
    for d in range(21):
        if day==7:
            signs = sign[3]
        elif day==1:
            signs = sign[9]
    for d in range(23,):
        if day==8:
            signs = sign[5]
        elif day==10:
            signs = sign[7]
        elif day==11:
            signs = sign[8]
    for d in range(22):
        if day==9:
            signs = sign[5]
        elif day==11:
            signs = sign[7]
        elif day==12:
            signs = sign[8]
    tel1 = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    tel2 = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    for a in range(1624,):           
        for j in range(12):
            for k in range(10):
                if a==1624+60*p:
                    tel=tel1[j*p] + tel2[k*p]
                else:
                    a+=p
                    tel=tel1[j*p] + tel2[k*p]
    print('うるう年です。'+str(day2)+'曜日です。星座は'+str(signs)+'です。十干十二支は'+str(tel)+'です。')
else:
    cipher = (o+n+day+d+i)%7
    day1 = ['土','日','月','火','水','木','金']
    day2 = day1[cipher]
    sign = ['牡羊座','牡牛座','双子座','蟹（かに）座','獅子座','乙女座','天秤座','蠍（サソリ）座','射手座','山羊座','水瓶座','魚（うお）座']
    for q in range(19,32):
        if day==2:
            signs = '魚（うお）座'
    for q in range(19):
        if day==3:
            signs = '魚（うお）座'
    for q in range(20,31):
        if day==4:
            signs = '牡牛座'
        elif day==9:
            signs = '天秤座'
    for q in range(20,32):
        if day==1:
            signs = '水瓶座'
    for q in range(20):
        if day==5:
            signs = '牡牛座'
        elif day==10:
            signs = '天秤座'    
        elif day==2:
            signs = '水瓶座'
    for q in range(21,32):
        if day==3:
            signs = '牡羊座'
        elif day==5:
            signs = '双子座'
    for q in range(21):
        if day==4:
            signs = '牡羊座'
        elif day==6:
            signs = '双子座'
    for q in range(22,31):
        if day==6:
            signs = '蟹（かに）座'
    for q in range(22,32):
        if day==12:
            signs = '山羊座'
    for q in range(22):
        if day==7:
            signs = '蟹（かに）座'
        elif day==1:
            signs = '山羊座'
    for q in range(23,32):
        if day==8:
            signs = '乙女座'
        elif day==10:
            signs = '蠍（サソリ）座'
    for q in range(23,31):
        if day==11:
            signs = '射手座'
    for q in range(23):
        if day==9:
            signs = '乙女座'
        elif day==11:
            signs = '蠍（サソリ）座'
        elif day==12:
            signs = '射手座'
    tel1 = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    tel2 = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    for a in range(1624,):           
        for j in range(12):
            for k in range(10):
                if a==1624+60*p:
                    tel=tel1[j*p] + tel2[k*p]
                else:
                    a+=p
                    tel=tel1[j*p] + tel2[k*p]
    print(str(day2)+'曜日です。星座は'+signs+'です。十干十二支は'+str(tel)+'です。')