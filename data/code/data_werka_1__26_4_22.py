class NumberChecker:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value
if __name__ == '__main__':
    num1 = NumberChecker(10)
    num2 = NumberChecker(5)
    print(num1.is_greater_than(num2))
    num3 = NumberChecker(3)
    num4 = NumberChecker(8)
    print(num3.is_greater_than(num4))