class NegativeChecker:
    @staticmethod
    def has_negative(numbers):
        return any(n < 0 for n in numbers)

if __name__ == '__main__':
    sample_values = [-1, 2, 3, -4, 5]
    print(NegativeChecker.has_negative(sample_values))