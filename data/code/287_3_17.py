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

    def convert_to(self, unit='kg'):
        if unit == 'kg':
            return [w for w in self.weights]
        elif unit == 'lbs':
            return [w / 0.453592 for w in self.weights]
        elif unit == 'oz':
            return [w / 0.0283495 for w in self.weights]

    def total_weight(self, unit='kg'):
        converted_weights = self.convert_to(unit)
        return sum(converted_weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(10, 'kg')
    wm.add_weight(2, 'lbs')
    wm.add_weight(35, 'oz')
    print("Total weight in kg:", wm.total_weight('kg'))
    print("Weights in lbs:", wm.convert_to('lbs'))