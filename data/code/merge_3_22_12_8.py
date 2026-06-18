class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_numbers = [1, 2, -3, 0, 5]
    
    for num in test_numbers:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")