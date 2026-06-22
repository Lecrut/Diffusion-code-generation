class IntegerChecker:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_greater_than(num1, num2):
        return num1 > num2

    def compare_with(self, other_number):
        if not isinstance(other_number, int):
            raise ValueError("The input must be an integer.")
        return IntegerChecker.is_greater_than(self.number, other_number)

if __name__ == '__main__':
    sample_num1 = 25
    sample_num2 = 12
    try:
        checker = IntegerChecker(sample_num1)
        result = checker.compare_with(sample_num2)
        print(result)
    except ValueError as e:
        print(e)