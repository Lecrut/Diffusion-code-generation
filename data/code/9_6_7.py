class VolumeConverter:
    def __init__(self):
        self.units = {
            'ml': 1.0,
            'l': 1000.0,
            'gal_us': 3785.411784,
            'gal_uk': 4546.09,
            'm3': 1000000.0,
            'ft3': 28316.846592,
            'in3': 16.387064,
            'tsp': 4.92892159375,
            'tbsp': 14.78676478125,
            'cup_us': 236.5882365,
            'barrel_oil': 158987.294928
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        value_in_ml = value * self.units[from_unit]
        result = value_in_ml / self.units[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 5.0
    source = 'l'
    target = 'gal_us'
    result = converter.convert(sample_value, source, target)
    print(f"{sample_value} {source} is {result} {target}")
    sample_value_2 = 1.0
    source_2 = 'm3'
    target_2 = 'gal_uk'
    result_2 = converter.convert(sample_value_2, source_2, target_2)
    print(f"{sample_value_2} {source_2} is {result_2} {target_2}")
    sample_value_3 = 1000.0
    source_3 = 'tsp'
    target_3 = 'ml'
    result_3 = converter.convert(sample_value_3, source_3, target_3)
    print(f"{sample_value_3} {source_3} is {result_3} {target_3}")