class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def validate_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weights cannot be negative")

    def compute_difference(self):
        self.validate_weight(self.weight1)
        self.validate_weight(self.weight2)
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_analyzer = WeightAnalyzer(15.5, 10.2)
    try:
        difference = weight_analyzer.compute_difference()
        print(difference)
    except (ValueError, TypeError) as e:
        print(e)