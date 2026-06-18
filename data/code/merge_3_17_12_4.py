class NumberChecker:
    def check_parity(self, num):
        if num % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input or command-line arguments
    sample_numbers = [1, 2, -3, 0]
    
    for number in sample_numbers:
        result = checker.check_parity(number)
        print(f"Number {number} is {result}")