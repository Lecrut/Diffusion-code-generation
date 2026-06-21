class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def heavier_person(self):
        if self.weight1 > self.weight2:
            return "Alice"
        elif self.weight2 > self.weight1:
            return "Bob"
        else:
            return "Both have the same weight"

if __name__ == '__main__':
    sample_weights = {'Alice': 75.5, 'Bob': 68.3}
    analyzer = WeightAnalyzer(sample_weights['Alice'], sample_weights['Bob'])
    difference = analyzer.calculate_difference()
    print(f"Weight Difference: {difference}")
    print(f"Heavier Person: {analyzer.heavier_person()}")