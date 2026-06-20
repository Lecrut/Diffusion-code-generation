class ZeroChecker:
    @staticmethod
    def is_zero(number):
        return number == 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5], [1, 0, 3, 4, 5], [10, 20, 30], [7, 8, 0, 9], []
    for values in sample_values:
        print(f"Sequence: {values}")
        result = any(ZeroChecker.is_zero(value) for value in values)
        print(result)