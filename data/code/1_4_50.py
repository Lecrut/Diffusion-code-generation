class WeightConverter:
    _CONVERSION_FACTORS = {
        ('pounds', 'kilograms'): 0.453592,
        ('kilograms', 'pounds'): 1 / 0.453592
    }

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        new_unit = new_unit.lower()
        if (self.unit, new_unit) in self._CONVERSION_FACTORS:
            conversion_factor = self._CONVERSION_FACTORS[(self.unit, new_unit)]
            return self.weight * conversion_factor
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")
    
    weight_in_kilograms = WeightConverter(68.0389, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")