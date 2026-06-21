class WeightComparison:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def describe_difference(self):
        difference = self.calculate_difference()
        if difference == 0:
            return "Both weights are the same."
        elif self.weight1 > self.weight2:
            return f"Alice is {difference} units heavier than Bob."
        else:
            return f"Bob is {difference} units heavier than Alice."

if __name__ == '__main__':
    sample_weights = {'Alice': 85.0, 'Bob': 79.2}
    comparison = WeightComparison(sample_weights['Alice'], sample_weights['Bob'])
    difference = comparison.calculate_difference()
    description = comparison.describe_difference()
    print(f"Weight Difference: {difference}")
    print(description)