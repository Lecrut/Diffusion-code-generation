class NumberComparator:

    @staticmethod
    def is_greater(num1, num2):
        return num1 > num2
if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 27
    result = NumberComparator.is_greater(sample_value1, sample_value2)
    print(result)
    test_cases = [(100, 50), (5, 10), (-5, -10), (0, 0), (3.14, 2.71), (-3.14, -2.71)]
    for num1, num2 in test_cases:
        result = NumberComparator.is_greater(num1, num2)
        print(f'NumberComparator.is_greater({num1}, {num2}) = {result}')