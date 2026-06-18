class NumberChecker:
    def check_odd(self, num):
        return num % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input
    sample_numbers = [17, -5, 42, 0]
    
    for number in sample_numbers:
        result = checker.check_odd(number)
        print(f"Is {number} odd? {result}")