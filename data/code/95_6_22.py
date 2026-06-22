class TripleCheck:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_positive(self, value):
        return value > 0

    def is_even(self, value):
        return value % 2 == 0

    def is_divisible(self, dividend, divisor):
        if divisor == 0:
            return False
        return dividend % divisor == 0

    def evaluate(self):
        cond1 = self.is_positive(self.a)
        cond2 = self.is_even(self.b)
        cond3 = self.is_divisible(self.c, self.a)
        return cond1 and cond2 and cond3

if __name__ == '__main__':
    obj = TripleCheck(3, 12, 36)
    print(obj.evaluate())
    
    obj2 = TripleCheck(-1, 12, 36)
    print(obj2.evaluate())
    
    obj3 = TripleCheck(3, 13, 36)
    print(obj3.evaluate())
    
    obj4 = TripleCheck(3, 12, 35)
    print(obj4.evaluate())