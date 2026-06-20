class NegativeChecker:
    @staticmethod
    def contains_negative(values):
        return any(value < 0 for value in values)

if __name__ == '__main__':
    sample_values = [10, -5, 0, -100]
    print(NegativeChecker.contains_negative(sample_values))