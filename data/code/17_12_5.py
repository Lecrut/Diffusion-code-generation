class NumberChecker:
    def check_parity(self, number):
        return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [10, 7, -4, 3]
    
    for value in test_values:
        result = checker.check_parity(value)
        print(f"Number {value} is {result}")