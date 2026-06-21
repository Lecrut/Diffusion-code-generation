class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()
    
    def _validate_unit(self, unit):
        if unit not in ['pounds', 'kilograms']:
            raise ValueError("Unsupported unit. Please use 'pounds' or 'kilograms'.")
    
    def convert_to(self, new_unit):
        self._validate_unit(new_unit)
        new_unit = new_unit.lower()
        
        if self.unit == 'pounds' and new_unit == 'kilograms':
            conversion_factor = 0.453592
        elif self.unit == 'kilograms' and new_unit == 'pounds':
            conversion_factor = 2.20462
        else:
            raise ValueError("Unsupported unit conversion")
        
        converted_weight = self.weight * conversion_factor
        return converted_weight

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")
    
    weight_in_kilograms = WeightConverter(68.039, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")