class NumberEvaluator:
    @staticmethod
    def is_positive(number):
        return number > 0

if __name__ == '__main__':
    test_values = [1, -1, 0, 2.5, -3.6]
    results = {value: NumberEvaluator.is_positive(value) for value in test_values}
    print(results)