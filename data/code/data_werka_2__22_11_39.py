class OddChecker:
    EVEN = 0

    @staticmethod
    def is_odd(n):
        return n % 2 != OddChecker.EVEN

if __name__ == '__main__':
    sample_values = [-10, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    for value in sample_values:
        print(f"{value} is odd: {OddChecker.is_odd(value)}")