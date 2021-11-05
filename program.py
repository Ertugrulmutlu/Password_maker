import random
from math import pi




class password:
    def creater(liste,no):
        for i in range(0,int(no)):
            random_number = random.randint(0,21)
            liste.append(number[random_number])
    def next(liste,special,integer):

        for i in range(0,len(liste)):
            for i2 in range(0,len(integer)):
                if liste[i] in special:
                    pass
                elif  liste[i] in integer:
                    number = liste[i]
                    number = int(liste[i]) * pi
                    liste.pop(i)
                    random_char.insert(i,str(number))
    
    def dot_deleter(liste):
        for i in range (0,len(liste)):
            a = liste[i]
            if '.' in a:
                for i2 in a:
                    if i2 == ".":
                        a = a.replace(".","")
                        liste.pop(i)
                        random_char.insert(i,str(a))

    def final(liste):
        password = ''.join(liste)
        return password





if __name__ == "__main__":
    no = input("How long do you want your password == ")
    number = ["1","2","3","4","5","6","7","8","9","@","$","*","/","l","e","t","m","e","f","r","e","e"]
    integer = ["1","2","3","4","5","6","7","8","9"]
    special = ["@","$","*","/"]
    random_char = []
    cla = password
    cla.creater(random_char,no)
    cla.next(random_char,special,integer)
    cla.dot_deleter(random_char)
    print(cla.final(random_char))




