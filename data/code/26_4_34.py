class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        if not isinstance(other, NumberChecker):
            raise ValueError("The other object must be an instance of NumberChecker")
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker(20)
    num2 = NumberChecker(15)
    result = num1.is_greater_than(num2)
    print(f"Is the value in num1 greater than the value in num2? {result}")