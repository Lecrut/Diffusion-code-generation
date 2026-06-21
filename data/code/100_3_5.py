class LogicChecker:
    _RESULT_MAP = {True: "All True", False: "Not All True"}

    def evaluate(self, bool_list):
        if not isinstance(bool_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        return all(bool_list)

    def get_status(self, bool_list):
        result = self.evaluate(bool_list)
        return self._RESULT_MAP.get(result, "Unknown")

if __name__ == '__main__':
    checker = LogicChecker()
    data_set = [True, True, True]
    print(checker.evaluate(data_set))
    print(checker.get_status(data_set))
    
    mixed_set = [True, False, True]
    print(checker.evaluate(mixed_set))
    print(checker.get_status(mixed_set))
    
    empty_set = []
    print(checker.evaluate(empty_set))
    print(checker.get_status(empty_set))