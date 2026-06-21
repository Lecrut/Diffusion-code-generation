class ParityChecker:
    EVEN = 0
    ODD = 1

    @staticmethod
    def is_odd(n):
        return n % 2 != 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, -3, 4, 5]
    results = {value: ParityChecker.is_odd(value) for value in sample_values}
    print(results)