class ComparisonUtility:
    @staticmethod
    def is_greater_than(num1, num2):
        return num1 > num2

if __name__ == '__main__':
    sample_num1 = 25
    sample_num2 = 10
    result = ComparisonUtility.is_greater_than(sample_num1, sample_num2)
    print(result)