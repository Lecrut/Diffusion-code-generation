class NumberChecker:
    """A class to check properties of integers."""

    def check_odd(self, number: int) -> bool:
        """Returns True if the number is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values to test without user input or file access
    samples = [17, 45, -3, 0, 8]

    for num in samples:
        result = checker.check_odd(num)
        print(f"{num} is {'odd' if result else 'even'}")