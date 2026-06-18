class NumberChecker:
    def check_odd(self, number):
        """Check if a given integer is odd."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values to test the class
    samples = [3, 4, -5, 10]
    
    for num in samples:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")