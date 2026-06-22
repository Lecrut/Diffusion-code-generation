class ValueComparator:
    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return self._compare_numbers(val1, val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return self._compare_strings(val1, val2)
        else:
            raise ValueError('Unsupported input types')

    def _compare_numbers(self, num1, num2):
        if num1 > num2:
            return (num1, 'greater', num2)
        elif num1 < num2:
            return (num2, 'greater', num1)
        else:
            return ('both', 'equal')

    def _compare_strings(self, str1, str2):
        if str1 > str2:
            return (str1, 'greater', str2)
        elif str1 < str2:
            return (str2, 'greater', str1)
        else:
            return ('both', 'equal')

if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(10, 5)
    result2 = comparator.compare_values('apple', 'banana')
    result3 = comparator.compare_values(3.14, 3.14)
    print(result1)
    print(result2)
    print(result3)