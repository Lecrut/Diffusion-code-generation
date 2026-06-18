class NumberChecker:
    def check_parity(self, num):
        if num % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input or network access
    samples = [4, 7, -3, 0]
    
    for num in samples:
        result = checker.check_parity(num)
        print(f"{num} is {result}")