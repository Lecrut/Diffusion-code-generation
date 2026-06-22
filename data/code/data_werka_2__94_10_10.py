class BooleanChecker:
    def __init__(self, initial_value, boolean_list):
        self.initial_value = initial_value
        self.boolean_list = boolean_list

    def check(self):
        if self.initial_value:
            return True
        for item in self.boolean_list:
            if item:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker(True, [False, False])
    print(checker.check())
    
    checker2 = BooleanChecker(False, [False, True])
    print(checker2.check())
    
    checker3 = BooleanChecker(False, [False, False])
    print(checker3.check())