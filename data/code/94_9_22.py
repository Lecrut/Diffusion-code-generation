class BooleanChecker:
    def __init__(self, data):
        self.data = list(data)

    def check_any_true(self):
        index = 0
        length = len(self.data)
        while index < length:
            if self.data[index]:
                return True
            index += 1
        return False

if __name__ == '__main__':
    checker_1 = BooleanChecker([False, False, True, False])
    print(checker_1.check_any_true())
    
    checker_2 = BooleanChecker([False, False, False])
    print(checker_2.check_any_true())
    
    checker_3 = BooleanChecker([])
    print(checker_3.check_any_true())
    
    checker_4 = BooleanChecker([True])
    print(checker_4.check_any_true())