class FalseChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check(self):
        return not self.a and not self.b

if __name__ == '__main__':
    checker1 = FalseChecker(False, False)
    print(checker1.check())
    
    checker2 = FalseChecker(True, False)
    print(checker2.check())
    
    checker3 = FalseChecker(False, True)
    print(checker3.check())
    
    checker4 = FalseChecker(True, True)
    print(checker4.check())