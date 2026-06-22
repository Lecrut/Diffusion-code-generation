class WeightManager:
    def __init__(self):
        self.weights = {'kg': [], 'lbs': [], 'oz': []}

    def add_weight(self, weight, unit):
        if unit not in ['kg', 'lbs', 'oz']:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")
        if unit == 'kg':
            self.weights['kg'].append(weight)
        elif unit == 'lbs':
            self.weights['kg'].append(weight * 0.453592)
        else:
            self.weights['kg'].append(weight * 0.0283495)

    def convert_to_kg(self):
        return sum(self.weights['kg'])

    def total_weight(self, unit='kg'):
        if unit == 'kg':
            return sum(self.weights['kg'])
        elif unit == 'lbs':
            return sum(w / 0.453592 for w in self.weights['kg'])
        elif unit == 'oz':
            return sum(w / 0.0283495 for w in self.weights['kg'])

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight('kg'))
    print("Total weight in lbs:", wm.total_weight('lbs'))