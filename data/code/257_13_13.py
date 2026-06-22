class ValueDifferenceCalculator:
    def __init__(self, data):
        if not isinstance(data, dict) or not all(isinstance(v, int) for v in data.values()):
            raise ValueError("Input must be a dictionary with integer values")
        self.data = data

    def calculate_difference(self):
        return max(self.data.values()) - min(self.data.values())

if __name__ == '__main__':
    calculator = ValueDifferenceCalculator({
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    })
    print(calculator.calculate_difference())