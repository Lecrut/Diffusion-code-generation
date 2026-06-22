class WeightManager:
    KGS_PER_LB = 0.453592
    KGS_PER_OZ = 0.0283495

    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(weight * self.KGS_PER_LB)
        elif unit == 'oz':
            self.weights.append(weight * self.KGS_PER_OZ)

    def convert_to_kg(self):
        return [weight for weight in self.weights]

    def total_weight(self):
        return sum(self.weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight (kg):", wm.total_weight())