class Fraction :
    def __init__(self, s = 0, m =1):
        self.s = s
        if m !=0 :
            self.m = m
        else:
            self.m = 1
    def show(self):
        print(self.s , '/', self.m)
    def mul(self,y):
        result = Fraction()
        result.s = self.s * y.s
        result.m = self.m * y.m
        return result
    
    def sum(self , other):
        result = Fraction()
        result.s = self.s * other.m + self.m * other.s
        result.m = self.m * other.m
        return result

    def sub(self ,other):
        result = Fraction()
        result.s = self.s * other.m - self.m * other.s
        result.m = self.m * other.m
        return result

    def div(self,other):
        result =Fraction()
        result.s =self.s * other.m
        result.m = self.m * other.s
        return result
        


a = Fraction(2,7)
a.show()
b = Fraction(3,4)
b.show
c = a.mul(b)
c.show()
d = a.sum(b)
d.show()
e = a.sub(b)
e.show()
f = a.div(b)
f.show()
