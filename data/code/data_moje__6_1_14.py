DIFFERENCE_PRECISION = 2

class WeightCalculator:
    def __init__(self):
        self.history = []

    def get_difference(self, w1, w2):
        diff = abs(w1 - w2)
        self.history.append(diff)
        return diff

    def get_last_result(self):
        return self.history[-1]

if __name__ == '__main__':
    calculator = WeightCalculator()
    val1 = 85.5
    val2 = 72.3
    result = calculator.get_difference(val1, val2)
    print(result)