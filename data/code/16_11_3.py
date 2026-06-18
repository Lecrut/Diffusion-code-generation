class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the provided numeric value is strictly positive.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()

# Hard-coded sample values for testing without user input or file access
test_values = [5, -3.5, 0, 1e-9, float('inf'), float('-inf')]

print("Testing check_positivity method:")
for val in test_values:
    result = checker.check_positivity(val)
    print(f"Value {val} is positive: {result}")