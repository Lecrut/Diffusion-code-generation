class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Test cases with hard-coded sample values
    test_numbers = [7, 10, -3, 0]
    
    for num in test_numbers:
        result = checker.check_odd(num)
        print(f"Number {num} is odd? {result}")