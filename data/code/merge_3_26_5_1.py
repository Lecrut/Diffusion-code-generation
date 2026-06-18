class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        """
        Compares this instance's value with another instance of NumberChecker.
        
        Args:
            other (NumberChecker): The instance to compare against.
            
        Returns:
            bool: True if self.value > other.value, False otherwise.
        """
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing the method without user input or external dependencies
    num1 = NumberChecker(10)
    num2 = NumberChecker(5)
    
    result1 = num1.is_greater_than(num2)
    print(f"Is 10 > 5? {result1}")

    result2 = num2.is_greater_than(num1)
    print(f"Is 5 > 10? {result2}")