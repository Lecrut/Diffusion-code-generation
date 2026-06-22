class NumberAnalyzer:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    sample_values = [-1, 2, -3.5, 0, 4.2]
    results = {value: NumberAnalyzer.is_negative(value) for value in sample_values}
    print(results)