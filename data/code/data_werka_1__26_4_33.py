class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker(20)
    num2 = NumberChecker(15)

    result1 = num1.is_greater_than(num2)
    print(f"Is {num1.value} greater than {num2.value}? {result1}")

    num3 = NumberChecker(10)
    num4 = NumberChecker(30)

    result2 = num3.is_greater_than(num4)
    print(f"Is {num3.value} greater than {num4.value}? {result2}")