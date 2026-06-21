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
        
        self.weight = converted_weight
        self.unit = new_unit.lower()
        return self.weight

if __name__ == '__main__':
    weight_converter = WeightConverter(100, 'pounds')
    print(f"Original weight: {weight_converter.weight} {weight_converter.unit}")
    
    try:
        converted_weight = weight_converter.convert_to('kilograms')
        print(f"Converted weight: {converted_weight} {weight_converter.unit}")
    except ValueError as e:
        print(e)