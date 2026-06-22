class PositiveChecker:
    @staticmethod
    def is_positive(num):
        return num > 0

    @classmethod
    def check_all_positive(cls, numbers):
        for number in numbers:
            if not cls.is_positive(number):
                return False
        return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = PositiveChecker.check_all_positive(sample_values)
    print(result)

    sample_values_with_negative = [1, -2, 3, 4, 5]
    result_with_negative = PositiveChecker.check_all_positive(sample_values_with_negative)
    print(result_with_negative)