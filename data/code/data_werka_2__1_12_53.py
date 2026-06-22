class WeightConverter:
    def __init__(self):
        self.conversion_factor = 2.20462

    def convert_kg_to_pounds(self, kg):
        return kg * self.conversion_factor

    def convert_pounds_to_kg(self, pounds):
        return pounds / self.conversion_factor

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weight_kg = 60
    sample_weight_pounds = 132
    
    converted_pounds = converter.convert_kg_to_pounds(sample_weight_kg)
    converted_kg = converter.convert_pounds_to_kg(sample_weight_pounds)
    
    print(f"{sample_weight_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_weight_pounds} pounds is {converted_kg:.2f} kg")