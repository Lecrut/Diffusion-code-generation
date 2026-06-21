class CheckEngine:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def is_positive(self):
        return self.first > 0

    def is_even(self):
        return self.second % 2 == 0

    def is_divisible(self):
        if self.first == 0:
            return False
        return self.third % self.first == 0

    def combine_checks(self):
        return self.is_positive() and self.is_even() and self.is_divisible()

if __name__ == '__main__':
    engine = CheckEngine(4, 8, 16)
    print(engine.combine_checks())
    
    engine2 = CheckEngine(3, 5, 12)
    print(engine2.combine_checks())
    
    engine3 = CheckEngine(-2, 4, 8)
    print(engine3.combine_checks())
    
    engine4 = CheckEngine(2, 3, 6)
    print(engine4.combine_checks())
    
    engine5 = CheckEngine(5, 10, 25)
    print(engine5.combine_checks())