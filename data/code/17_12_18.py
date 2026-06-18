class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [4, 7, -3, 10]
    
    for value in test_values:
        result = checker.check_parity(value)
        print(f"{value} is {result}")