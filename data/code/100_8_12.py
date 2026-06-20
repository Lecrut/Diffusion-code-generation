class NumberComparison:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def check_condition(self):
        return (self.num1 + self.num2) > abs(self.num1 - self.num2)

if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 5
    comparison_instance = NumberComparison(sample_num1, sample_num2)
    result = comparison_instance.check_condition()
    print(result)