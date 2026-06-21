class OddEvaluator:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

if __name__ == '__main__':
    sample_values = [0, -1, 3, 8, 15, 22]
    results = {value: OddEvaluator.is_odd(value) for value in sample_values}
    print(results)