class WeightManager:
    CONVERSIONS = {
        'kg': 1,
        'lbs': 0.453592,
        'oz': 0.0283495
    }

    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit not in self.CONVERSIONS:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")
        self.weights.append(weight * self.CONVERSIONS[unit])

    def convert_to_kg(self):
        return [weight / self.CONVERSIONS['kg'] for weight in self.weights]

    def total_weight(self):
        return sum(self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight (kg):", wm.total_weight())