class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'miles_to_km': 1.60934,
            'km_to_miles': 1 / 1.60934
        }

    def adjust_distance(self, distance, unit):
        if unit == 'miles':
            adjusted_distance = distance * self.conversion_factors['miles_to_km']
            new_unit = 'km'
        elif unit == 'km':
            adjusted_distance = distance * self.conversion_factors['km_to_miles']
            new_unit = 'miles'
        else:
            raise ValueError("Unsupported unit type")
        return adjusted_distance, new_unit

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_distance_miles = 5
    adjusted_distance_km, new_unit_km = converter.adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 10
    adjusted_distance_miles, new_unit_miles = converter.adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")