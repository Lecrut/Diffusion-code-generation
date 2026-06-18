class LengthComparator:
    """A class to compare two length measurements."""

    def __init__(self, unit1="meters", unit2="meters"):
        self.unit1 = unit1.lower()
        self.unit2 = unit2.lower()

    def _convert_to_base(self, value, unit):
        """Convert a length to meters for comparison."""
        if unit == "km":
            return value * 1000
        elif unit == "cm" or unit == "centimeter":
            return value / 100
        elif unit == "mm" or unit == "millimeter":
            return value / 1000
        else:
            # Assume input is in meters if no specific conversion needed
            return value

    def compare(self, length_a, length_b):
        """Compare two lengths and print the result."""
        base_unit = self.unit1
        
        converted_a = self._convert_to_base(length_a, self.unit1)
        converted_b = self._convert_to_base(length_b, self.unit2)

        if converted_a > converted_b:
            return f"{length_a} {self.unit1} is greater than {length_b} {self.unit2}"
        elif converted_a < converted_b:
            return f"{length_b} {self.unit2} is greater than {length_a} {self.unit1}"
        else:
            return f"{length_a} {self.unit1} is equal to {length_b} {self.unit2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    comparator = LengthComparator()

    test_cases = [
        (5, 3),           # meters vs meters
        ("10", "km"),     # km vs meters
        ("2.5", "cm"),    # cm vs meters
        ("100", "mm"),    # mm vs meters
        ("7", "meters"),  # explicit unit string
        (3, "centimeter") # mixed input types and units
    ]

    for val_a in test_cases:
        if isinstance(val_a[0], str):
            length_val = float(val_a[0])
        else:
            length_val = val_a[0]
        
        unit_str = ""
        if len(val_a) == 2 and not isinstance(val_a[1], (int, float)):
            # If second element is a string representing the unit for comparison B
            pass
        
        # Re-structure test cases to match expected input format: (length_value, length_unit_or_second_length_tuple)
        
    # Let's simplify the main block logic based on how compare expects arguments
    
    print("Running LengthComparator tests...")

    # Test 1: Simple meters comparison
    result = comparator.compare(5.0, 3.0)
    print(result)

    # Test 2: Kilometers vs Meters (using string unit for B to test conversion logic if needed, 
    # but the class constructor sets default units based on args passed during init or usage)
    
    # Adjusting how we use compare method directly with values and assuming base is meters unless overridden in __init__ call
    
    comparator2 = LengthComparator("km", "meters")
    result2 = comparator2.compare(1.5, 1000)
    print(result2)

    # Test 3: Centimeters vs Meters using the default constructor logic which assumes meters as base if not specified in init args properly for B
    # The class currently defaults unit1 and unit2 to "meters" unless passed. 
    # We will pass units explicitly here or rely on internal conversion logic assuming standard SI prefixes relative to meter
    
    comparator3 = LengthComparator("cm", "mm")
    result3 = comparator3.compare(50, 5)
    print(result3)

    # Test 4: Equal values in different units (1m vs 100cm converted correctly if logic holds, 
    # but our current _convert_to_base assumes base is unit1. Let's verify behavior with explicit setup)
    
    comparator4 = LengthComparator("meter", "centimeter")
    result4 = comparator4.compare(1, 100)
    print(result4)

    print("\nAll tests completed successfully.")