class ParityChecker:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return (self.value & 1) == 0

if __name__ == '__main__':
    checker = ParityChecker(42)
    print(checker.is_even())
    
    checker2 = ParityChecker(15)
    print(checker2.is_even())
    
    checker3 = ParityChecker(-8)
    print(checker3.is_even())