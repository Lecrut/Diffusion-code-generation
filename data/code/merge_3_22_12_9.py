class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test values
    numbers_to_check = [15, 42, -3, 0]
    
    for num in numbers_to_check:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")