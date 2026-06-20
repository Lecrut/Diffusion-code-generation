class AttributeChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @staticmethod
    def is_positive(value):
        return value > 0
    
    @staticmethod
    def is_even(value):
        return value % 2 == 0
    
    @staticmethod
    def is_divisible(dividend, divisor):
        return dividend % divisor == 0
    
    def check_attributes(self):
        return (self.is_positive(self.a) and
                self.is_even(self.b) and
                self.is_divisible(self.c, self.a))

if __name__ == '__main__':
    checker = AttributeChecker(5, 4, 10)
    print(checker.check_attributes())