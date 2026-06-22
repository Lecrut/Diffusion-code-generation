KG_TO_LBS = 2.20462
LBS_TO_KG = 1 / KG_TO_LBS
KG_TO_OZ = 35.274
OZ_TO_KG = 1 / KG_TO_OZ

class WeightManager:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight, unit):
        if unit == 'kg':
            self.weights.append(weight)
        elif unit == 'lbs':
            self.weights.append(KG_TO_LBS * weight)
        elif unit == 'oz':
            self.weights.append(KG_TO_OZ * weight)
        else:
            raise ValueError("Invalid unit. Use 'kg', 'lbs', or 'oz'.")

    def convert_to(self, target_unit):
        if target_unit == 'kg':
            return [w for w in self.weights]
        elif target_unit == 'lbs':
            return [KG_TO_LBS * w for w in self.weights]
        elif target_unit == 'oz':
            return [KG_TO_OZ * w for w in self.weights]
        else:
            raise ValueError("Invalid target unit. Use 'kg', 'lbs', or 'oz'.")

    def total_weight(self, unit='kg'):
        if unit == 'kg':
            return sum(self.weights)
        elif unit == 'lbs':
            return sum(KG_TO_LBS * w for w in self.weights)
        elif unit == 'oz':
            return sum(KG_TO_OZ * w for w in self.weights)
        else:
            raise ValueError("Invalid target unit. Use 'kg', 'lbs', or 'oz'.")

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight(1, 'kg')
    wm.add_weight(2.20462, 'lbs')
    print("Total weight in kg:", wm.total_weight())
    print("Weights converted to lbs:", wm.convert_to('lbs'))