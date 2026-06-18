class NumberChecker:
    def check_odd(self, number):
        """Check if a given integer is odd."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [17, 42, -3, 0, 99]
    
    print("Testing check_odd method:")
    for val in test_values:
        result = checker.check_odd(val)
        status = "Odd" if result else "Even"
        print(f"{val}: {status}")