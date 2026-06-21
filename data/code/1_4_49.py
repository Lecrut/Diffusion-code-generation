class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            conversion_factor = 0.453592
            return WeightConverter(self.weight * conversion_factor, 'kilograms')
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            conversion_factor = 2.20462
            return WeightConverter(self.weight * conversion_factor, 'pounds')
        else:
            raise ValueError("Unsupported unit conversion")

    def __str__(self):
        return f"{self.weight} {self.unit}"

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    print(weight_in_pounds)
    
    converted_weight = weight_in_pounds.convert_to('kilograms')
    print(converted_weight)