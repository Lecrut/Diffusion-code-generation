class OddityChecker:
    def is_odd(self, number):
        return number % 2 == 1

if __name__ == '__main__':
    checker = OddityChecker()
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for value in sample_values:
        print(f"{value} is {'Odd' if checker.is_odd(value) else 'Even'}")