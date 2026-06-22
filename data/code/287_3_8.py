class WeightManager:
    KG_TO_LBS = 2.20462
    LBS_TO_KG = 1 / KG_TO_LBS
    KG_TO_OZ = 35.274
    OZ_TO_KG = 1 / KG_TO_OZ

    def __init__(self):
        self.weights_in_kg = []

    @staticmethod
    def convert_to_kg(weight, unit):
        if unit == 'kg':
            return weight
        elif unit == 'lbs':
            return weight * WeightManager.LBS_TO_KG
        elif unit == 'oz':
            return weight * WeightManager.OZ_TO_KG
        else:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")

    def add_weight(self, weight, unit):
        self.weights_in_kg.append(self.convert_to_kg(weight, unit))

    def convert_to(self, target_unit='kg'):
        if target_unit == 'kg':
            return [w for w in self.weights_in_kg]
        elif target_unit == 'lbs':
            return [w * WeightManager.KG_TO_LBS for w in self.weights_in_kg]
        elif target_unit == 'oz':
            return [w * WeightManager.KG_TO_OZ for w in self.weights_in_kg]
        else:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")

    def total_weight(self, unit='kg'):
        weights = self.convert_to(unit)
        return sum(weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Weights in kg:", wm.weights_in_kg)
    print("Total weight (kg):", wm.total_weight('kg'))
    print("Total weight (lbs):", wm.total_weight('lbs'))