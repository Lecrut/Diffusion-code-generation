class NumberChecker:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value
if __name__ == '__main__':
    num1_value = 20
    num2_value = 15
    number1 = NumberChecker(num1_value)
    number2 = NumberChecker(num2_value)
    is_greater = number1.is_greater_than(number2)
    print(is_greater)