class LogicChecker:
    def evaluate(self, bool_list):
        if not bool_list:
            return True
        result = bool_list[0]
        index = 1
        length = len(bool_list)
        while index < length:
            if not bool_list[index]:
                return False
            result = result and bool_list[index]
            index += 1
        return result

if __name__ == '__main__':
    checker = LogicChecker()
    test_data = [True, True, True, True]
    test_data_false = [True, False, True, True]
    test_data_empty = []
    test_data_single = [True]
    print(checker.evaluate(test_data))
    print(checker.evaluate(test_data_false))
    print(checker.evaluate(test_data_empty))
    print(checker.evaluate(test_data_single))