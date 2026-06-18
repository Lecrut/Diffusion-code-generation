class NumberChecker:
    def check_odd(self, number):
        """Returns True if the given integer is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input
    test_numbers = [17, -3, 0, 4, 8]

    print("Testing NumberChecker.check_odd method:")
    for num in test_numbers:
        result = checker.check_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num} is {status}")