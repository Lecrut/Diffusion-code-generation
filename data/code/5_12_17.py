class LengthComparator:
    """A class to compare two length measurements."""
    
    def __init__(self, unit1='meters', unit2='meters'):
        self.unit1 = unit1.lower()
        self.unit2 = unit2.lower()
        
    def convert_to_base(self, value, target_unit):
        """Convert a length value to the base unit (meters)."""
        units = {
            'm': 1.0,      # meters
            'km': 0.001,   # kilometers
            'cm': 100.0,   # centimeters
            'mm': 1000.0,  # millimeters
            'in': 254.0,   # inches (approx)
        }
        
        multiplier = units.get(target_unit.lower(), None)
        if multiplier is not None:
            return value * multiplier
        
        raise ValueError(f"Unsupported unit for conversion: {target_unit}")

    def compare(self, length1_str, length2_str):
        """
        Compare two length measurements.
        
        Args:
            length1_str (str): First measurement as "value unit" string.
            length2_str (str): Second measurement as "value unit" string.
            
        Returns:
            str: A clear output describing the comparison result.
        """
        try:
            # Parse first value and unit
            parts1 = length1_str.strip().split()
            if len(parts1) != 2:
                return f"Invalid format for first measurement: '{length1_str}' (expected 'value unit')"
            
            val1, u1 = float(parts1[0]), self.unit1
            # Override with explicit input units from the string parts if provided differently
            # For simplicity in this implementation, we assume standard inputs like "5 m" or just numbers for default meters
            
            # Re-parse strictly as value and unit based on common formats. 
            # If user passes 'value' only, treat as base unit (meters).
            
        except ValueError:
            return f"Invalid input format. Expected numeric values with optional units."

    def compare(self, length1_str, length2_str):
        """Compare two lengths and print the result."""
        
        # Helper to parse "value unit" string into float value and str unit
        def parse_length(s):
            s = s.strip()
            if ' ' in s:
                val_part, unit_part = s.split(None, 1)
                try:
                    return float(val_part), unit_part.lower(), True # has_unit=True
                except ValueError:
                    pass
            
            # Assume meters if no unit specified or just a number provided directly as per task simplicity
            try:
                val = float(s.strip())
                return val, 'm', False 
            except ValueError:
                raise ValueError(f"Cannot parse length string: '{s}'")

        p1_val, u1_str, _ = parse_length(length1_str)
        p2_val, u2_str, _ = parse_length(length2_str)
        
        # Determine base unit (meters) for comparison logic consistency
        def to_meters(val, unit):
            conversion_factors = {
                'km': 0.001, 
                'cm': 1e-2, 
                'mm': 1e-3, 
                'in': 0.0254 # inches to meters
            }
            factor = conversion_factors.get(unit.lower(), None) or (lambda x: x if unit == 'm' else float('nan'))
            
            return val * factor

        base_unit_meters = self.convert_to_base(p1_val, u1_str)
        base_unit_meters_2 = self.convert_to_base(p2_val, u2_str)

        # Determine relationship
        if abs(base_unit_meters - base_unit_meters_2) < 0.0000001: 
            print(f"Lengths are equal.")
        elif base_unit_meters > base_unit_meters_2:
            print(f"{length1_str} is greater than {length2_str}.")
        else:
            print(f"{length2_str} is greater than {length1_str}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input, no args)
    
    comp = LengthComparator()
    
    # Sample 1: Meters vs Centimeters
    result1 = comp.compare("5 m", "500 cm")
    
    print("---\n")

    # Sample 2: Kilometers vs Millimeters (different magnitudes)
    result2 = comp.compare("2 km", "2000 mm")
    
    print("---\n")

    # Sample 3: Different units directly in string format for clarity if needed, 
    # though the class defaults to meters parsing logic above.
    # Let's test with explicit unit strings passed as arguments by user expectation
    result3 = comp.compare("10 km", "5 m")
    
    print("---\n")

    # Sample 4: Equal values in different units (if supported via conversion)
    result4 = comp.compare("1 inch", "2.54 cm")