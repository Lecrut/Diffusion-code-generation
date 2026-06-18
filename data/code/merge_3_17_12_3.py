class NumberChecker:
    def check_parity(self, number):
        """Returns 'Even' if the number is even, otherwise returns 'Odd'."""
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test values run without user input or external dependencies
    samples = [10, 7, -4, 0]
    
    for num in samples:
        result = checker.check_parity(num)
        print(f"Number {num} is {result}")