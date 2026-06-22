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

    def convert_to(self, target_unit):
        conversion_factors = {'kg': 1, 'lbs': 0.453592, 'oz': 0.0283495}
        if target_unit not in conversion_factors:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")
        return [weight / conversion_factors[target_unit] for weight in self.weights]

    def total_weight(self):
        return sum(self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight())
    print("Weights in lbs:", wm.convert_to('lbs'))