class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return self._compare_numeric(val1, val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return self._compare_strings(val1, val2)
        else:
            raise ValueError('Unsupported input types')

    def _compare_numeric(self, num1, num2):
        return (num1 > num2, num1 < num2, num1 == num2)

    def _compare_strings(self, str1, str2):
        return (str1 > str2, str1 < str2, str1 == str2)
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(20, 30)
    result2 = comparator.compare_values('cat', 'dog')
    result3 = comparator.compare_values(5.5, 5.5)
    print(result1)
    print(result2)
    print(result3)