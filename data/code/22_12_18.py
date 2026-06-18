class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test
    test_numbers = [5, 4, -3, 0]
    
    for num in test_numbers:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")