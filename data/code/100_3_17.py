class LogicChecker:
    EXPECTED_RESULT = True
    DEFAULT_INPUT = [True, True, True]
    
    def evaluate(self, bool_list):
        if not bool_list:
            return self.EXPECTED_RESULT
        current_state = self.EXPECTED_RESULT
        for item in bool_list:
            if not item:
                return False
            current_state = current_state and item
        return current_state

if __name__ == '__main__':
    checker = LogicChecker()
    test_data = [True, True, True]
    result = checker.evaluate(test_data)
    print(result)