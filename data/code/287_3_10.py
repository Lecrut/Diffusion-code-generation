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
        if target_unit == 'kg':
            return [weight for weight in self.weights]
        elif target_unit == 'lbs':
            return [weight / 0.453592 for weight in self.weights]
        elif target_unit == 'oz':
            return [weight / 0.0283495 for weight in self.weights]

    def total_weight(self, unit='kg'):
        converted_weights = self.convert_to(unit)
        return sum(converted_weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight('kg'))
    print("Total weight in lbs:", wm.total_weight('lbs'))