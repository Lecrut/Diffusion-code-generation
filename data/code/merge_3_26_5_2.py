class NumberChecker:
    def is_greater_than(self, other):
        """Returns True if self.value > other.value, False otherwise."""
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing
    num1 = NumberChecker()
    num2 = NumberChecker()

    num1.value = 50
    num2.value = 30

    result = num1.is_greater_than(num2)
    
    print(f"{num1.value} > {num2.value}? Result: {result}")