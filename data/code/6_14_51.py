class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def check_weights(self):
        if self.weight1 < 0 or self.weight2 < 0:
            raise ValueError("Weights cannot be negative")
        return True

    def calculate_difference(self):
        if not self.check_weights():
            return None
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_analyzer = WeightAnalyzer(20.3, 5.8)
    try:
        difference = weight_analyzer.calculate_difference()
        print(f"The weight difference is: {difference}")
    except ValueError as e:
        print(e)