class DistanceConverter:
    MILES_TO_KM = 1.60934

    def __init__(self):
        self.conversion_factors = {
            'miles': self.MILES_TO_KM,
            'km': 1 / self.MILES_TO_KM
        }

    def adjust_distance(self, distance, unit):
        if unit not in self.conversion_factors:
            raise ValueError("Unsupported unit type")
        adjusted_distance = distance * self.conversion_factors[unit]
        new_unit = 'km' if unit == 'miles' else 'miles'
        return adjusted_distance, new_unit

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_distance_miles = 6
    adjusted_distance_km, new_unit_km = converter.adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 12
    adjusted_distance_miles, new_unit_miles = converter.adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")