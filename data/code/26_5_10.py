class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        """Returns True if self.value > other.value, else False."""
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker(50)
    num2 = NumberChecker(30)
    
    result = num1.is_greater_than(num2)
    print(f"{num1.value} is greater than {num2.value}: {result}")

    # Additional test case where the condition might be false
    num3 = NumberChecker(25)
    result_false = num1.is_greater_than(num3)
    print(f"{num1.value} is greater than {num3.value}: {result_false}")