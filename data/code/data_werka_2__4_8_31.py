class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            ('miles', 'kilometers'): 1.60934,
            ('kilometers', 'miles'): 0.621371
        }

    def convert(self, distance, unit_from, unit_to):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
        
        conversion_key = (unit_from.lower(), unit_to.lower())
        if conversion_key in self.conversion_factors:
            return distance * self.conversion_factors[conversion_key]
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter()
    
    miles_distance = 10
    kilometers_distance = converter.convert(miles_distance, 'miles', 'kilometers')
    print(f"{miles_distance} miles is {kilometers_distance} kilometers")