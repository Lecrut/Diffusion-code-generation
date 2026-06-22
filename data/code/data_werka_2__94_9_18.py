class BooleanChecker:
    def __init__(self, data):
        self.data = data

    def check_any_true(self):
        iterator = iter(self.data)
        try:
            while True:
                item = next(iterator)
                if item:
                    return True
        except StopIteration:
            return False

if __name__ == '__main__':
    checker1 = BooleanChecker([False, False, False])
    print(checker1.check_any_true())
    
    checker2 = BooleanChecker([False, True, False])
    print(checker2.check_any_true())
    
    checker3 = BooleanChecker([])
    print(checker3.check_any_true())
    
    checker4 = BooleanChecker([True])
    print(checker4.check_any_true())