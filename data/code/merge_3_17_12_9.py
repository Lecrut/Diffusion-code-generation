class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test the method without user input
    sample_numbers = [10, 7, -4, 23]
    
    for num in sample_numbers:
        result = checker.check_parity(num)
        print(f"{num} is {result}")