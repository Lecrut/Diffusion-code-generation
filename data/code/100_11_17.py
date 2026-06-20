class LogicChecker:
    TRUE = True
    FALSE = False

    @staticmethod
    def are_all_true(bool_list):
        return all((item == LogicChecker.TRUE for item in bool_list))

    @staticmethod
    def are_all_false(bool_list):
        return all((item == LogicChecker.FALSE for item in bool_list))
if __name__ == '__main__':
    sample_values = [True, True, True]
    print(LogicChecker.are_all_true(sample_values))
    sample_values = [False, False, False]
    print(LogicChecker.are_all_false(sample_values))
    sample_values = [True, False, True]
    print(LogicChecker.are_all_true(sample_values))
    sample_values = [True, True, False]
    print(LogicChecker.are_all_false(sample_values))