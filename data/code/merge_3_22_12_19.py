class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test
    test_cases = [1, 2, -3, 0, 5]
    
    for num in test_cases:
        result = checker.check_odd(num)
        print(f"{num} is odd: {result}")