class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    def convert_to(self, target_unit):
        if self.unit == 'pounds' and target_unit == 'kilograms':
            conversion_factor = 0.453592
        elif self.unit == 'kilograms' and target_unit == 'pounds':
            conversion_factor = 2.20462
        else:
            raise ValueError("Unsupported unit conversion")

        converted_weight = self.weight * conversion_factor
        return WeightConverter(converted_weight, target_unit)

    def __str__(self):
        return f"{self.weight} {self.unit}"

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    print(f"Original weight: {weight_in_pounds}")

    converted_to_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Converted to kilograms: {converted_to_kg}")