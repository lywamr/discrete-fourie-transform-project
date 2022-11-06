import math


class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pow(self, n):
        if n == 0:
            return Complex(1, 0)
        answer = self
        for i in range(1, n):
            answer = answer.product(self)
        return answer

    def add(self, c):
        a = self.a + c.a
        b = self.b + c.b
        return Complex(a, b)


    def product(self, c):
        a = (self.a * c.a) - (self.b * c.b)
        b = (self.a * c.b) + (self.b * c.a)
        return Complex(a, b)

    def to_string(self):
        answer = ""
        if self.b == 0:
            answer = self.a
        elif self.b < 0:
            answer = "{real:.5f} - {image:.5f}i".format(
                real=self.a, image=abs(self.b))
        else:
            answer = "{real:.5f}  + {image:.5f}i".format(
                real=self.a, image=abs(self.b))
        return answer


def cis(x):
    a = math.cos(x)
    b = math.sin(x)
    c = Complex(a, b)
    return c


def wk(k, n):
    answer = cis(2*k*math.pi / n)
    return answer


def string_to_complex(s):
    does_have_plus_sign = '+' in s
    if does_have_plus_sign:
        sign = "+"
        a = int(s.split(sign)[0])
        b = int(s.split(sign)[1].split("i")[0])
    else:
        sign = "-"
        a = int(s.split(sign)[0])
        b = (-1)*int(s.split(sign)[1].split("i")[0])
    c = Complex(a, b)
    return c

print("Laya Amirian  - IUST - DFT project \n")

print("please enter the value of n  (n > 0 and n is an integer ) : ->\n ")
n = int(input())
arr_a = []
arr_b = []
w_s = []
for i in range(0, n):
    print("a[{x}] -> (please type your inputs exactly in the format of a+bi)".format(x=i))
    s = input()
    c = string_to_complex(s)
    arr_a.append(c)

    wi = wk(i, n)
    w_s.append(wi)

for i in range(0, n):
    bi = Complex(0, 0)
    for j in range(0, n):
        x = arr_a[j]
        w = w_s[i].pow(j)
        bi = bi.add(x.product(w))
    arr_b.append(bi)

for i in range(0, n):
    print("[+] b[{index}] is : {s}".format(index=i, s=arr_b[i].to_string()))

print ("******************** have a nice day ******************")
