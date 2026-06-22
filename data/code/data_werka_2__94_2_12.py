class BooleanChecker:
    TARGET_VALUE = True

    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        
        for item in boolean_list:
            if item is self.TARGET_VALUE:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    data_set_1 = [False, False, False]
    data_set_2 = [False, True, False]
    data_set_3 = []
    data_set_4 = [False, False, True, False]
    
    result_1 = checker.has_at_least_one_true(data_set_1)
    result_2 = checker.has_at_least_one_true(data_set_2)
    result_3 = checker.has_at_least_one_true(data_set_3)
    result_4 = checker.has_at_least_one_true(data_set_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)