KG_TO_LBS = 2.20462
KG_TO_OZ = 35.274

class WeightManager:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(weight / KG_TO_LBS)
        elif unit == 'oz':
            self.weights.append(weight / KG_TO_OZ)

    def convert_to_kg(self):
        return [weight for weight in self.weights]

    def total_weight(self, unit='kg'):
        if unit == 'kg':
            return sum(self.weights)
        elif unit == 'lbs':
            return sum(w * KG_TO_LBS for w in self.weights)
        elif unit == 'oz':
            return sum(w * KG_TO_OZ for w in self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight('kg'))