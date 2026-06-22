class WeightConverter:

    def convert_kg_to_lbs(self, kilograms):
        return kilograms * 2.20462
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.convert_kg_to_lbs(1.0))
    print(converter.convert_kg_to_lbs(5.0))