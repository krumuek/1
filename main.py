#ตัวอย่างที่ 1
list1=["สมชาย","สมหมาย","สมปอง","สมใจ"]
for name in list1 :
  print("นาย",name)
print("จบการทำงาน")
print('\n')

#ตัวอย่างที่ 2 โปรแกรมคำนวณการหารจ่ายค่าอาหาร
i=int(input("คุณต้องการคำนวณกี่รอบครับ"))
for count in range(i) :               #ให้ตัวแปร count เก็บค่าตาม list ที่มีจำนวนตาม i
  print("การคำนวณรอบที่",count+1)       #ที่ต้องบวก 1 เพราะโปรแกรมจะเริ่มที่ตำแหน่ง 0 เสมอ
  total=int(input("ราคาอาหารทั้งหมด"))
  number=int(input("จำนวนผู้รับประทานอาหาร"))
  avg=total/number
  print("จ่ายค่าอาหารคนละ",avg,"บาท")
print("จบการทำงาน")