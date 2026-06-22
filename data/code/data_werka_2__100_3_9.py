class LogicChecker:
    EXPECTED_STATE = True
    RESULT_TRUE = "True"
    RESULT_FALSE = "False"

    def evaluate(self, bool_list):
        if not bool_list:
            return self.EXPECTED_STATE
        current_state = self.EXPECTED_STATE
        for item in bool_list:
            if item is not self.EXPECTED_STATE:
                current_state = not self.EXPECTED_STATE
                break
        return current_state

if __name__ == '__main__':
    checker = LogicChecker()
    data_set_a = [True, True, True]
    data_set_b = [True, False, True]
    data_set_c = [False, False, False]
    data_set_d = []
    data_set_e = [True]

    res_a = checker.evaluate(data_set_a)
    res_b = checker.evaluate(data_set_b)
    res_c = checker.evaluate(data_set_c)
    res_d = checker.evaluate(data_set_d)
    res_e = checker.evaluate(data_set_e)

    print(f"A: {res_a}")
    print(f"B: {res_b}")
    print(f"C: {res_c}")
    print(f"D: {res_d}")
    print(f"E: {res_e}")