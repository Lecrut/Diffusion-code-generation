class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    num1_value = 20
    num2_value = 15
    num1 = NumberChecker(num1_value)
    num2 = NumberChecker(num2_value)
    
    result = num1.is_greater_than(num2)
    print(f"Is {num1.value} greater than {num2.value}? {result}")