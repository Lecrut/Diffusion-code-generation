class NumberChecker:
    def __init__(self, value):
        self.value = value

    def compare_to(self, other):
        return self.value > other.value

if __name__ == '__main__':
    VALUE_THRESHOLD = 7
    num1 = NumberChecker(10)
    num2 = NumberChecker(5)
    print(num1.compare_to(num2))

    num3 = NumberChecker(VALUE_THRESHOLD + 1)
    num4 = NumberChecker(VALUE_THRESHOLD)
    print(num3.compare_to(num4))