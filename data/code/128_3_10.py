class NegativeChecker:
    def __init__(self, num):
        self.num = num
    
    def is_negative(self):
        return self.num < 0

if __name__ == '__main__':
    checker1 = NegativeChecker(-5)
    print(checker1.is_negative())
    
    checker2 = NegativeChecker(0)
    print(checker2.is_negative())
    
    checker3 = NegativeChecker(10)
    print(checker3.is_negative())