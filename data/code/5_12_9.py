class LengthComparator:
    """A class to compare two length measurements."""
    
    def __init__(self, unit_a='meters', unit_b='metres'):
        self.unit_a = unit_a.lower() if isinstance(unit_a, str) else 'meters'
        self.unit_b = unit_b.lower() if isinstance(unit_b, str) else 'metres'

    def compare(self, val1, unit):
        """Convert a length to meters and return the value in base units."""
        conversion_factors = {
            'millimeter': 0.001,
            'centimeter': 0.01,
            'meter': 1.0,
            'kilometer': 1000.0,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.34,
        }

        if unit.lower() not in conversion_factors:
            raise ValueError(f"Unsupported length unit: {unit}")

        return val1 * conversion_factors[unit.lower()]

if __name__ == '__main__':
    # Hard-coded sample values for testing
    comp = LengthComparator(unit_a='meter', unit_b='foot')

    print("Comparing lengths (converting both to meters):")
    
    length_meters = 10.5
    length_feet = 20.3
    
    meter_val = comp.compare(length_meters, "meters")
    foot_to_meter_val = comp.compare(length_feet, "feet")

    if meter_val > foot_to_meter_val:
        print(f"{length_meters} meters is greater than {length_feet} feet.")
    elif length_feet > length_meters:
        print(f"{length_feet} feet is greater than {length_meters} meters.")
    else:
        print(f"{length_meters} meters is equal to {length_feet} feet.")

    # Additional comparison without conversion for display purposes
    print("\nDirect values:")
    if length_meters > length_feet:
        print("10.5 meters is greater than 20.3 (raw numbers).")
    elif length_feet > length_meters:
        print("20.3 feet is greater than 10.5 meters.")
    else:
        print(f"{length_meters} == {length_feet}")