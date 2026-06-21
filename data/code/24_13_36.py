class NumberEvaluator:
    @staticmethod
    def is_negative(value):
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    sample_values = [-10, 5, -3.14, 2.71, 'hello', None]
    results = {value: NumberEvaluator.is_negative(value) for value in sample_values}
    print(results)