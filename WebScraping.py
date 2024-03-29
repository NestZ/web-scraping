# -*- coding: utf-8 -*-
file1 = open("data.txt","w")
import requests
import time
ar = ['เชียงของ','เทิง','พาน','ป่าแดด','แม่จัน','เชียงแสน','แม่สาย','แม่สรวย','เวียงป่าเป้า','พญาเม็งราย','เวียงแก่น','ขุนตาล','แม่ฟ้าหลวง','แม่ลาว','เวียงเชียงรุ้ง','ดอยหลวง']
tr = [['บุญเรือง','ห้วยซ้อ','ศรีดอนชัย','ริมโขง'],
      ['เวียง','งิ้ว','ปล้อง','แม่ลอย','เชียงเคี่ยน','ตับเต่า','หงาว','สันทรายงาม','ศรีดอนไชย','หนองแรด'],
      ['สันมะเค็ด','แม่อ้อ','ธารทอง','สันติสุข','ดอยงาม','หัวง้ม','เจริญเมือง','ป่าหุ่ง','ม่วงคำ','ทรายขาว','สันกลาง','แม่เย็น','เมืองพาน','ทานตะวัน','เวียงห้าว'],
      ['ป่าแดด','ป่าแงะ','สันมะค่า','โรงช้าง','ศรีโพธิ์เงิน'],
      ['แม่จัน','จันจว้า','แม่คำ','ป่าซาง','สันทราย','ท่าข้าวเปลือก','ป่าตึง','แม่ไร่','ศรีค้ำ','จันจว้าใต้','จอมสวรรค์'],
      ['เวียง','ป่าสัก','บ้านแซว','ศรีดอนมูล','แม่เงิน','โยนก'],
      ['แม่สาย','ห้วยไคร้','เกาะช้าง','โป่งผา','ศรีเมืองชุม','เวียงพางคำ','บ้านด้าย','โป่งงาม'],
      ['แม่สรวย','ป่าแดด','แม่พริก','ศรีถ้อย','ท่าก๊อ','วาวี','เจดีย์หลวง'],
      ['สันสลี','เวียง','บ้านโป่ง','ป่างิ้ว','เวียงกาหลง','แม่เจดีย์','แม่เจดีย์ใหม่'],
      ['แม่เปา','แม่ต๋ำ','ไม้ยา','เม็งราย','ตาดควัน'],
      ['ม่วงยาย','ปอ','หล่ายงาว','ท่าข้าม'],
      ['ต้า','ป่าตาล','ยางฮอม'],
      ['เทอดไทย','แม่สลองใน','แม่สลองนอก','แม่ฟ้าหลวง'],
      ['ดงมะดะ','จอมหมอกแก้ว','บัวสลี','ป่าก่อดำ','โป่งแพร่'],
      ['ทุ่งก่อ','ดงมหาวัน','ป่าซาง'],
      ['ปงน้อย','โชคชัย','หนองป่าก่อ']]

from bs4 import BeautifulSoup
p = 'เชียงราย'
count = 0
for i in ar:
    for j in tr[count]:
        file1.writelines('ต.' + j + ' อ.' + i + '\n')
        url = "http://www.noplink.com/postcode_t.php?t=" + j + "&a=" + i + "&p=" + p
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        x = soup.find_all("td")[26]
        for k in range(2,len(x.find_all("tr")) - 1):
                a = x.find_all("tr")[k]
                for l in range(0,2):
                    c = a.find_all("td")[abs(l - 1)]
                    print c.text
                    L = c.text.encode('utf-8')
                    file1.writelines(L + ' ')
                file1.writelines('\n')
    count += 1
    time.sleep(10)
