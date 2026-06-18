class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input
    sample_numbers = [5, 4, -3, 10]
    
    for num in sample_numbers:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")