class WeightConverter:
    POUNDS_TO_KG = 0.453592
    KG_TO_POUNDS = 1 / POUNDS_TO_KG

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    @staticmethod
    def convert(weight, from_unit, to_unit):
        if from_unit == 'pounds' and to_unit == 'kilograms':
            return weight * WeightConverter.POUNDS_TO_KG
        elif from_unit == 'kilograms' and to_unit == 'pounds':
            return weight * WeightConverter.KG_TO_POUNDS
        else:
            raise ValueError("Unsupported unit conversion")

    def change_unit(self, new_unit):
        self.weight = WeightConverter.convert(self.weight, self.unit, new_unit)
        self.unit = new_unit.lower()

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    weight_in_pounds.change_unit('kilograms')
    print(f"Weight in kilograms: {weight_in_pounds.weight} kg")

    weight_in_kilograms = WeightConverter(68.039, 'kilograms')
    weight_in_kilograms.change_unit('pounds')
    print(f"Weight in pounds: {weight_in_kilograms.weight} lbs")