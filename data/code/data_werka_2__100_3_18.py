class LogicChecker:
    def evaluate(self, bool_list):
        result = True
        index = 0
        length = len(bool_list)
        while index < length:
            current_value = bool_list[index]
            if current_value is False:
                result = False
                break
            index += 1
        return result

if __name__ == '__main__':
    checker = LogicChecker()
    test_data_a = [True, True, True]
    test_data_b = [True, False, True]
    test_data_c = [False, False, False]
    test_data_d = [True]
    test_data_e = []
    print(checker.evaluate(test_data_a))
    print(checker.evaluate(test_data_b))
    print(checker.evaluate(test_data_c))
    print(checker.evaluate(test_data_d))
    print(checker.evaluate(test_data_e))