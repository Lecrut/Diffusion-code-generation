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

    def convert_to(self, target_unit):
        if target_unit not in ['kg', 'lbs', 'oz']:
            raise ValueError("Invalid target unit. Use 'kg', 'lbs', or 'oz'.")
        conversion_factors = {
            'kg': 1,
            'lbs': 0.453592,
            'oz': 0.0283495
        }
        factor = conversion_factors[target_unit] / conversion_factors[self._get_default_unit()]
        return [weight * factor for weight in self.weights]

    def _get_default_unit(self):
        if len(self.weights) == 0:
            raise ValueError("No weights added yet.")
        return 'kg' if all(isinstance(w, (int, float)) and w >= 0 for w in self.weights) else 'oz'

    def total_weight(self, unit='kg'):
        converted_weights = self.convert_to(unit)
        return sum(converted_weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight('kg'))
    print("Total weight in lbs:", wm.total_weight('lbs'))