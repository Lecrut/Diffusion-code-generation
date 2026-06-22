class WeightManager:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(weight * 0.453592)
        elif unit == 'oz':
            self.weights.append(weight * 0.0283495)

    def convert_to_kg(self):
        return [weight for weight in self.weights]

    def total_weight(self):
        return sum(self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    wm.add_weight(35.274, 'oz')
    print("Weights in kg:", wm.convert_to_kg())
    print("Total weight:", wm.total_weight(), "kg")