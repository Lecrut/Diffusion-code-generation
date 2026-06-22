class NumberComparator:
    @staticmethod
    def is_larger(num1, num2):
        return num1 > num2

if __name__ == '__main__':
    sample_value1 = 75
    sample_value2 = 30
    result = NumberComparator.is_larger(sample_value1, sample_value2)
    print(result)