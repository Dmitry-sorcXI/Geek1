#time_list = [60,60,24,24]
#word_list = [" сек", " мин" , " час" , " дн"]
#res_list = []
#num = int(input("Ввод: "))

#for ind , ver in enumerate(time_list):       
    #res_list.append(str(num % ver) + word_list[ind])
   # num //= ver

   # len_list = len(res_list) - 1
   # while len_list >= 0:
       # print(res_list[len_list], end=" ")
        #len_list -=1


seconds = int(input("Введите секунды: "))
days = seconds // 3600 //24
hours = seconds // 3600 - days * 24
minutes = seconds // 60 % 60 
second = seconds % 60 

print (days , " Дней " , hours , " Часов " , minutes , " Минут ", "и " , second , " остаточных секунд.", sep="")