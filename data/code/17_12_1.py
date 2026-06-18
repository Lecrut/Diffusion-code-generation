class NumberChecker:
    def check_parity(self, number):
        return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    test_cases = [10, 7, -4, 0]
    
    for num in test_cases:
        result = checker.check_parity(num)
        print(f"{num} is {result}")