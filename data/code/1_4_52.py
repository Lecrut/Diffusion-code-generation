class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def _validate_unit(self, unit):
        if unit not in ['pounds', 'kilograms']:
            raise ValueError("Unsupported unit. Use 'pounds' or 'kilograms'.")

    def convert_to(self, new_unit):
        self._validate_unit(new_unit)
        new_unit = new_unit.lower()
        
        if self.unit == new_unit:
            return self.weight

        conversion_factors = {
            ('pounds', 'kilograms'): 0.453592,
            ('kilograms', 'pounds'): 2.20462
        }

        key = (self.unit, new_unit)
        if key in conversion_factors:
            return self.weight * conversion_factors[key]
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")

    weight_in_kilograms = WeightConverter(68.0389, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")