class WeightConverter:
    def __init__(self, value, unit='pounds'):
        self.value = value
        self.unit = unit.lower()
        self._validate_unit(self.unit)

    def _validate_unit(self, unit):
        valid_units = ['pounds', 'kilograms', 'grams', 'ounces']
        if unit not in valid_units:
            raise ValueError(f"Unsupported unit: {unit}")

    def change_unit(self, new_unit):
        new_unit = new_unit.lower()
        self._validate_unit(new_unit)
        self.value = self._convert(self.value, self.unit, new_unit)
        self.unit = new_unit
        return self.value

    def _convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        conversion_factors = {
            ('pounds', 'kilograms'): 0.453592,
            ('pounds', 'grams'): 453.592,
            ('pounds', 'ounces'): 16.0,
            ('kilograms', 'pounds'): 2.20462,
            ('kilograms', 'grams'): 1000.0,
            ('kilograms', 'ounces'): 35.274,
            ('grams', 'pounds'): 0.00220462,
            ('grams', 'kilograms'): 0.001,
            ('grams', 'ounces'): 0.035274,
            ('ounces', 'pounds'): 0.0625,
            ('ounces', 'kilograms'): 0.0283495,
            ('ounces', 'grams'): 28.3495
        }

        if (from_unit, to_unit) in conversion_factors:
            return value * conversion_factors[(from_unit, to_unit)]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

    def get_weight(self):
        return self.value, self.unit

if __name__ == '__main__':
    weight = WeightConverter(150, 'pounds')
    print(weight.get_weight())
    converted_value = weight.change_unit('kilograms')
    print(converted_value)
    print(weight.get_weight())
    converted_value_grams = weight.change_unit('grams')
    print(converted_value_grams)
    print(weight.get_weight())