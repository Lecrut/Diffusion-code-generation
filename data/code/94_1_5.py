class BooleanChecker:
    def __init__(self, data):
        self.data = data

    def check_any_true(self):
        if not self.data:
            return False
        for val in self.data:
            if val is True or val is False:
                if val:
                    return True
            else:
                if val:
                    return True
        return False

if __name__ == '__main__':
    checker1 = BooleanChecker([False, False, False])
    print(checker1.check_any_true())
    
    checker2 = BooleanChecker([False, True, False])
    print(checker2.check_any_true())
    
    checker3 = BooleanChecker([])
    print(checker3.check_any_true())