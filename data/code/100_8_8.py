class NumberComparison:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def check_condition(self):
        return (self.sum_is_greater()) and (self.diff_is_positive())

    def sum_is_greater(self):
        return self.num1 + self.num2 > 0

    def diff_is_positive(self):
        return abs(self.num1 - self.num2) > 0

if __name__ == '__main__':
    sample_num1 = 5
    sample_num2 = 3
    comparison_instance = NumberComparison(sample_num1, sample_num2)
    outcome = comparison_instance.check_condition()
    print(outcome)