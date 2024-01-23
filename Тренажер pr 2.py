import random
import time

x=1
while x !=2:
    operation = input("Выберите тренажер (+/-)")


    if operation =='+':
        correct=0
        incorrect=0
        start_time=time.time()
        
        k=0
        while k<=19:
            for x in range(1):
                a=random.randint(0,100)
                b=random.randint(0,100)
                if a+b <= 100 and a+b >=1:
                    k+=1
                    c=round(a+b, 1)
                    print(f"Сколько будет {a} + {b}")
                    answer= eval(input("Мой ответ это "))
                    if answer == c:
                        print("Правильно!")
                        correct+=1
                    else:
                        print('Неправильно')
                        incorrect+=1
                        print("Верный ответ:"+ str(a+b))
        persent = str(correct/(correct+incorrect)*100)
        pr=persent[:-2]
        end_time=time.time()
        full_time=(end_time-start_time)
        print(f"У тебя верно решено {correct} из {incorrect} примеров, ты набрал {pr}%")
        print("Время:" + str(full_time) + "сек.")


    if operation =='-':
        correct=0
        incorrect=0
        start_time=time.time()
        k1=0
        while k1<=19:
            for x in range(1):
                a=random.randint(0,100)
                b=random.randint(0,100)
                if a+b <= 100:
                    k1+=1
                    c=round(a-b, 1)
                    print(f"Сколько будет {a} - {b}")
                    answer= eval(input("Мой ответ это "))
                    if answer == c:
                        print("Правильно!")
                        correct+=1
                    else:
                        print('Неправильно')
                        incorrect+=1
                        print("Верный ответ:"+ str(a-b))
        persent = str(correct/(correct+incorrect)*100)
        pr=persent[:-2]
        end_time=time.time()
        full_time=(end_time-start_time)
        print(f"У тебя верно решено {correct} из {incorrect} примеров, ты набрал {pr}%")
        print("Время:" + str(full_time) + "сек.")
