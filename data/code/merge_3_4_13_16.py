class DistanceConverter:
    def __init__(self):
        # Base unit is meters (m)
        self.meters_per_mile = 1609.344
        self.kilometers_per_meter = 0.001
    
    def convert_to_base(self, distance_value, from_unit):
        """Convert any input unit to the base unit (meters)."""
        if not isinstance(distance_value, (int, float)):
            raise TypeError("Distance value must be a number")
        
        conversion_factors = {
            'mile': self.meters_per_mile,
            'kilometer': 1000.0,
            'meter': 1.0
        }
        
        if from_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: '{from_unit}'. Supported units are mile, kilometer, meter.")
            
        return distance_value * conversion_factors[from_unit]
    
    def convert_to_target(self, base_meters, to_unit):
        """Convert the base unit (meters) back to any target unit."""
        if not isinstance(base_meters, (int, float)):
            raise TypeError("Base meter value must be a number")
        
        conversion_factors = {
            'mile': 1.0 / self.meters_per_mile,
            'kilometer': 0.001,
            'meter': 1.0
        }
        
        if to_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: '{to_unit}'. Supported units are mile, kilometer, meter.")
            
        return base_meters * conversion_factors[to_unit]
    
    def convert(self, value, from_unit, to_unit):
        """Seamlessly convert distance between any pair of specified units."""
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be a number")
        
        base_value = self.convert_to_base(value, from_unit)
        result = self.convert_to_target(base_value, to_unit)
        return result

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample conversion 1: Miles to Kilometers
    miles_input = 5.0
    km_result = converter.convert(miles_input, 'mile', 'kilometer')
    
    print(f"Converting {miles_input} mile(s) to kilometers")
    print(f"Result: {km_result:.4f} kilometer(s)")

    # Sample conversion 2: Meters to Miles
    meters_input = 100.0
    miles_result = converter.convert(meters_input, 'meter', 'mile')
    
    print(f"\nConverting {meters_input} meter(s) to miles")
    print(f"Result: {miles_result:.4f} mile(s)")

    # Sample conversion 3: Kilometers to Meters (Round trip check concept)
    km_input = 10.5
    meters_from_km = converter.convert(km_input, 'kilometer', 'meter')
    
    print(f"\nConverting {km_input} kilometer(s) to meters")
    print(f"Result: {meters_from_km:.4f} meter(s)")