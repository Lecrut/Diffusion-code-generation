class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters': 1.0,
            'feet': 3.28084,
            'kilometers': 0.001
        }

    def convert(self, length, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return length * self.conversion_factors[target_unit]

if __name__ == '__main__':
    converter = LengthConverter()
    
    sample_length_meters = 100
    converted_to_feet = converter.convert(sample_length_meters, 'feet')
    print(f"{sample_length_meters} meters is {converted_to_feet} feet")
    
    sample_length_kilometers = 50
    converted_to_meters = converter.convert(sample_length_kilometers, 'meters')
    print(f"{sample_length_kilometers} kilometers is {converted_to_meters} meters")
    
    sample_length_feet = 300
    converted_to_meters = converter.convert(sample_length_feet, 'meters')
    print(f"{sample_length_feet} feet is {converted_to_meters} meters")