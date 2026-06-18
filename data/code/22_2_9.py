class NumberChecker:
    def check_odd(self, number):
        """Returns True if 'number' is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values to test the class
    samples = [13, 45, -7, 28, 0]
    
    for num in samples:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")