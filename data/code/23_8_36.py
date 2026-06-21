class ValueComparator:
    NUMERIC_TYPES = (int, float)
    STRING_TYPES = (str,)

    @staticmethod
    def _compare_numeric(val1, val2):
        return (val1 > val2, val1 < val2, val1 == val2)

    @staticmethod
    def _compare_string(val1, val2):
        return (val1 > val2, val1 < val2, val1 == val2)

    def compare_values(self, val1, val2):
        if isinstance(val1, self.NUMERIC_TYPES) and isinstance(val2, self.NUMERIC_TYPES):
            return self._compare_numeric(val1, val2)
        elif isinstance(val1, self.STRING_TYPES) and isinstance(val2, self.STRING_TYPES):
            return self._compare_string(val1, val2)
        else:
            raise ValueError('Unsupported input types')
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(10, 5)
    result2 = comparator.compare_values('apple', 'banana')
    result3 = comparator.compare_values(3.14, 3.14)
    print(result1)
    print(result2)
    print(result3)