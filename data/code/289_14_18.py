class NauticalMilesConverter:
    conversion_factor = 1.852
    
    @staticmethod
    def nautical_miles_to_kilometers(nautical_miles):
        if not isinstance(nautical_miles, (int, float)):
            raise ValueError("Input must be an integer or floating-point number")
        return round(nautical_miles * NauticalMilesConverter.conversion_factor, 2)

if __name__ == '__main__':
    converter = NauticalMilesConverter()
    print(converter.nautical_miles_to_kilometers(10))
    print(converter.nautical_miles_to_kilometers(5.5))
    print(converter.nautical_miles_to_kilometers(3.75))