class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return self._compare_numeric(val1, val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return self._compare_string(val1, val2)
        else:
            raise ValueError('Unsupported input types')

    def _compare_numeric(self, num1, num2):
        if num1 > num2:
            return (True, False, False)
        elif num1 < num2:
            return (False, True, False)
        else:
            return (False, False, True)

    def _compare_string(self, str1, str2):
        if str1 > str2:
            return (True, False, False)
        elif str1 < str2:
            return (False, True, False)
        else:
            return (False, False, True)
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(7, 3)
    result2 = comparator.compare_values('orange', 'grape')
    result3 = comparator.compare_values(5.0, 5.0)
    print(result1)
    print(result2)
    print(result3)