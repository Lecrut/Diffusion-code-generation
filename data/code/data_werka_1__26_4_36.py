class NumberChecker:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or float")
        self.value = value

    def is_greater_than(self, other):
        if not isinstance(other, NumberChecker):
            raise TypeError("Other must be an instance of NumberChecker")
        return self.value > other.value

if __name__ == '__main__':
    try:
        num1 = NumberChecker(20)
        num2 = NumberChecker(15)
        result = num1.is_greater_than(num2)
        print(f"Is num1 ({num1.value}) greater than num2 ({num2.value}): {result}")
    except (ValueError, TypeError) as e:
        print(e)