class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371
    
    def __init__(self):
        self.conversion_factors = {
            ('miles', 'kilometers'): DistanceConverter.MILES_TO_KILOMETERS,
            ('kilometers', 'miles'): DistanceConverter.KILOMETERS_TO_MILES
        }
    
    def validate_distance(self, distance):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
    
    def validate_units(self, unit_from, unit_to):
        valid_units = {'miles', 'kilometers'}
        if unit_from.lower() not in valid_units or unit_to.lower() not in valid_units:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")
    
    def convert(self, distance, unit_from, unit_to):
        self.validate_distance(distance)
        self.validate_units(unit_from, unit_to)
        
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()
        conversion_key = (unit_from, unit_to)
        
        if conversion_key in self.conversion_factors:
            return distance * self.conversion_factors[conversion_key]
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")
    
if __name__ == '__main__':
    converter = DistanceConverter()
    miles_distance = 10
    kilometers_distance = 16.0934
    
    print(f"{miles_distance} miles is {converter.convert(miles_distance, 'miles', 'kilometers')} kilometers")
    print(f"{kilometers_distance} kilometers is {converter.convert(kilometers_distance, 'kilometers', 'miles')} miles")