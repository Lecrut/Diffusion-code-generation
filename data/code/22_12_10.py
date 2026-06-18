class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    samples = [7, 10, -3, 0]
    
    for num in samples:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")