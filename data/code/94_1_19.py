class BooleanChecker:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def _validate_input(iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("Input must be an iterable")
        return iterable

    @staticmethod
    def _check_element(element):
        return element is BooleanChecker.TRUE_VALUE

    @classmethod
    def check_any_true(cls, iterable):
        validated = cls._validate_input(iterable)
        for element in validated:
            if cls._check_element(element):
                return True
        return False

if __name__ == '__main__':
    data_sets = [
        [False, False, True, False],
        [False, False, False],
        [True],
        [],
        [False, False, False, False]
    ]
    for data in data_sets:
        result = BooleanChecker.check_any_true(data)
        print(result)