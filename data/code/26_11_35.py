class NumberComparator:
    @staticmethod
    def is_greater(num1, num2):
        return num1 > num2

if __name__ == '__main__':
    sample_value1 = 15
    sample_value2 = 8
    result = NumberComparator.is_greater(sample_value1, sample_value2)
    print(result)