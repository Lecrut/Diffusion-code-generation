class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [17, 42, -3, 0]
    
    for value in test_values:
        result = checker.check_odd(value)
        print(f"Is {value} odd? {result}")