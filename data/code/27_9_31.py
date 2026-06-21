class ValueChecker:

    def __init__(self):
        self.comparison_map = {'integer': lambda x, y: x != y, 'string': lambda x, y: x != y, 'float': lambda x, y: x != y}

    def are_different(self, val1, val2):
        val_type = type(val1).__name__
        if val_type not in self.comparison_map:
            raise ValueError(f'Unsupported type: {val_type}')
        return self.comparison_map[val_type](val1, val2)
if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(10, 20)
    result_str = checker.are_different('hello', 'world')
    result_float = checker.are_different(3.14, 2.71)
    print(result_int)
    print(result_str)
    print(result_float)