class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return (self.value & 1) == 0

if __name__ == '__main__':
    checker = NumberChecker(8)
    print(checker.is_even())
    
    checker2 = NumberChecker(9)
    print(checker2.is_even())