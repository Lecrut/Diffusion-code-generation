class WeightManager:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit not in ['kg', 'lbs', 'oz']:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(weight * 0.453592)
        else:
            self.weights.append(weight * 0.0283495)

    def convert_to_kg(self):
        return [weight for weight in self.weights]

    def total_weight(self):
        return sum(self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight())