class WeightManager:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit='kg'):
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(weight * 0.453592)
        elif unit == 'oz':
            self.weights.append(weight * 0.0283495)

    def convert_to_kg(self):
        return [weight / 0.453592 for weight in self.weights]

    def total_weight(self, unit='kg'):
        if unit == 'kg':
            return sum(self.weights)
        elif unit == 'lbs':
            return sum(weight * 0.453592 for weight in self.weights)
        elif unit == 'oz':
            return sum(weight * 0.0283495 for weight in self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2, 'lbs')
    wm.add_weight(16, 'oz')
    print("Total weight (kg):", wm.total_weight('kg'))
    print("Converted weights (kg):", wm.convert_to_kg())