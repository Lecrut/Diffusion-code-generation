class NumberChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    sample_values = [-10, 5, 0, -2.718, 3.14159]
    results = {value: NumberChecker.is_negative(value) for value in sample_values}
    print(results)