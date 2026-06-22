class NumberChecker:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value
if __name__ == '__main__':
    sample_values = {'number1': 20, 'number2': 30}
    number1 = NumberChecker(sample_values['number1'])
    number2 = NumberChecker(sample_values['number2'])
    result = number1.is_greater_than(number2)
    print(f"Is {sample_values['number1']} greater than {sample_values['number2']}: {result}")