class NumberChecker:
    def check_parity(self, number):
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, 7, 0, -3, 42]
    for value in sample_values:
        result = checker.check_parity(value)
        print(f"The number {value} is {result}.")