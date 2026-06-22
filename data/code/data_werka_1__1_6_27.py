class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if self.unit == 'pounds' and target_unit == 'kilograms':
            conversion_factor = 0.453592
            return WeightConverter(self.weight * conversion_factor, target_unit)
        elif self.unit == 'kilograms' and target_unit == 'pounds':
            conversion_factor = 2.20462
            return WeightConverter(self.weight * conversion_factor, target_unit)
        else:
            raise ValueError("Unsupported unit conversion")

    def __str__(self):
        return f"{self.weight} {self.unit}"

if __name__ == '__main__':
    weight_in_pounds = 150
    converter = WeightConverter(weight_in_pounds, 'pounds')
    converted_weight = converter.convert_to('kilograms')
    print(converted_weight)