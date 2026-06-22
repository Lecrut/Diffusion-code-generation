class LogicChecker:
    _VALID_TYPES = (bool,)

    def evaluate(self, bool_list):
        if not isinstance(bool_list, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        for item in bool_list:
            if not isinstance(item, self._VALID_TYPES):
                raise ValueError(f"Invalid boolean type: {type(item)}")
        result = True
        for item in bool_list:
            if not item:
                result = False
                break
        return result

if __name__ == '__main__':
    checker = LogicChecker()
    samples = [
        [True, True, True],
        [True, False, True],
        [False, False],
        [],
        [True]
    ]
    for s in samples:
        print(checker.evaluate(s))