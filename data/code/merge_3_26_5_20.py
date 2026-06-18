class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        """Returns True if self.value > other.value, False otherwise."""
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    num1 = NumberChecker(50)
    num2 = NumberChecker(30)
    
    result = num1.is_greater_than(num2)
    
    print(f"{num1.value} > {num2.value}: {result}")