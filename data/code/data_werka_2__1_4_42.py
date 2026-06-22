class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            converted_weight = self.weight * 0.453592
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            converted_weight = self.weight / 0.453592
        else:
            raise ValueError("Unsupported unit conversion")
        
        return converted_weight

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(100, 'pounds')
    print(f"Weight in kilograms: {weight_in_pounds.convert_to('kilograms')}")

    weight_in_kilograms = WeightConverter(45.3592, 'kilograms')
    print(f"Weight in pounds: {weight_in_kilograms.convert_to('pounds')}")