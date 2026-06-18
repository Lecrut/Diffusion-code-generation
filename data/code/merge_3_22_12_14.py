class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input or network access
    test_values = [17, -5, 42, 0, 3]
    
    for value in test_values:
        result = checker.check_odd(value)
        print(f"Is {value} odd? {result}")