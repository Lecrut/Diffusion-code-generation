class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    sample_values = [1, 4, -3, 0]
    
    for num in sample_values:
        result = checker.check_parity(num)
        print(f"{num} is {result}")