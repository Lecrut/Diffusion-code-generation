class ValueChecker:

    def __init__(self):
        self.type_checks = {int: lambda x, y: x != y, float: lambda x, y: x != y, str: lambda x, y: x != y}

    def are_different(self, val1, val2):
        if type(val1) not in self.type_checks or type(val2) not in self.type_checks:
            raise ValueError(f'Unsupported type: {type(val1).__name__} or {type(val2).__name__}')
        return self.type_checks[type(val1)](val1, val2)
if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(45, 67)
    result_str = checker.are_different('apple', 'banana')
    result_float = checker.are_different(1.23, 4.56)
    print(result_int)
    print(result_str)
    print(result_float)