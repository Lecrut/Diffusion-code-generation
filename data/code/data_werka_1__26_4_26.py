class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    number1 = NumberChecker(10)
    number2 = NumberChecker(5)
    result = number1.is_greater_than(number2)
    print(result)