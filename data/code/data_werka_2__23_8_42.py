class ValueComparator:

    def compare_values(self, val1, val2):
        self._validate_inputs(val1, val2)
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return self._compare_numeric(val1, val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return self._compare_strings(val1, val2)
        else:
            raise ValueError('Unsupported input types')

    def _validate_inputs(self, val1, val2):
        if not (isinstance(val1, (int, float)) or isinstance(val1, str)):
            raise ValueError(f'Unsupported type for val1: {type(val1)}')
        if not (isinstance(val2, (int, float)) or isinstance(val2, str)):
            raise ValueError(f'Unsupported type for val2: {type(val2)}')

    def _compare_numeric(self, val1, val2):
        return (val1 > val2, val1 < val2, val1 == val2)

    def _compare_strings(self, val1, val2):
        return (val1 > val2, val1 < val2, val1 == val2)
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(50, 20)
    result2 = comparator.compare_values('orange', 'apple')
    result3 = comparator.compare_values(7.5, 7.5)
    print(result1)
    print(result2)
    print(result3)