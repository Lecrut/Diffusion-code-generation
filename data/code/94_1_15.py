class BooleanChecker:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def _validate_input(iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("Input must be an iterable")
        return iterable

    @staticmethod
    def check_any_true(iterable):
        validated = BooleanChecker._validate_input(iterable)
        result = False
        for element in validated:
            if element is BooleanChecker.TRUE_VALUE:
                result = True
                break
        return result

if __name__ == '__main__':
    sample_data = [False, False, False, False]
    output = BooleanChecker.check_any_true(sample_data)
    print(output)