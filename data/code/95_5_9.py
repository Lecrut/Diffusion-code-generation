class IntegerChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        is_positive = self.a > 0
        is_even = self.b % 2 == 0
        divisor = self.a
        is_divisible = False
        if divisor != 0:
            is_divisible = self.c % divisor == 0
        return (is_positive, is_even, is_divisible)

if __name__ == '__main__':
    checker = IntegerChecker(7, 8, 14)
    print(checker.check())
    
    checker2 = IntegerChecker(-3, 5, 10)
    print(checker2.check())
    
    checker3 = IntegerChecker(0, 10, 0)
    print(checker3.check())