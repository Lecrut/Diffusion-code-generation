class NumberChecker:
    def check_odd(self, number):
        """Returns True if 'number' is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    sample_numbers = [17, -5, 42, 0]
    
    for num in sample_numbers:
        result = checker.check_odd(num)
        print(f"{num} is {'odd' if result else 'even'}")