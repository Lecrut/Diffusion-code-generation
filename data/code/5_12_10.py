class LengthComparator:
    def compare(self, length1_value, unit1, length2_value, unit2):
        """
        Compares two length measurements by converting them to a common base (meters).
        
        Supported units: 'cm', 'mm', 'km' (case-insensitive)
        Conversion factors relative to meters: 1 cm = 0.01 m, 1 mm = 0.001 m, 1 km = 1000 m
        
        Returns a string indicating the relationship between the two lengths.
        """
        # Define conversion factors for supported units
        conversions = {
            'cm': 0.01,
            'mm': 0.001,
            'km': 1000
        }

        def to_meters(value, unit):
            unit_lower = unit.lower()
            if unit_lower not in conversions:
                raise ValueError(f"Unsupported length unit: {unit}. Supported units are cm, mm, km.")
            return value * conversions[unit_lower]

        # Convert both lengths to meters for comparison
        val1_meters = to_meters(length1_value, unit1)
        val2_meters = to_meters(length2_value, unit2)

        if abs(val1_meters - val2_meters) < 0.00001: # Float tolerance
            return f"Equal (within {val1_meters:.6f} and {val2_meters:.6f})"
        elif val1_meters > val2_meters:
            difference = val1_meters - val2_meters

if __name__ == '__main__':
    pass
