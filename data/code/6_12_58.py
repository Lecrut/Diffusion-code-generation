class WeightComparator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def describe_weights(self):
        if self.weight1 > self.weight2:
            return "Alice is heavier than Bob."
        elif self.weight2 > self.weight1:
            return "Bob is heavier than Alice."
        else:
            return "Both Alice and Bob have the same weight."

if __name__ == '__main__':
    alice_weight = 75.5
    bob_weight = 68.3
    comparator = WeightComparator(alice_weight, bob_weight)
    
    difference = comparator.calculate_difference()
    description = comparator.describe_weights()

    print(f"Weight Difference: {difference}")
    print(description)