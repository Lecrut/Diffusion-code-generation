class BooleanListChecker:
    def __init__(self, bool_list):
        if not isinstance(bool_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for item in bool_list:
            if not isinstance(item, bool):
                raise ValueError("All elements must be booleans")
        self._data = list(bool_list)

    def has_true(self):
        if not self._data:
            return False
        return True in self._data

def check_any_true(bool_list):
    checker = BooleanListChecker(bool_list)
    return checker.has_true()

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    sample_empty = []
    result = check_any_true(sample_data)
    result_empty = check_any_true(sample_empty)
    print(result)
    print(result_empty)