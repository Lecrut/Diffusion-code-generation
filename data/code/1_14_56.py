class WeightConverter:
    _CONVERSION_TABLE = {
        'kg_to_pounds': 2.20462,
        'pounds_to_kg': 1 / 2.20462
    }
    
    def convert(self, value, conversion_type):
        if conversion_type not in self._CONVERSION_TABLE:
            raise ValueError("Unsupported conversion type")
        return value * self._CONVERSION_TABLE[conversion_type]

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 90
    sample_pounds = 198.426
    
    converted_pounds = converter.convert(sample_kg, 'kg_to_pounds')
    converted_kg = converter.convert(sample_pounds, 'pounds_to_kg')
    
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")