class NumberChecker:
    def check_parity(self, num):
        """Returns 'Even' if number is even, otherwise returns 'Odd'."""
        return "Even" if num % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [10, 7, -4, 0]
    
    for value in test_values:
        result = checker.check_parity(value)
        print(f"{value} is {result}")