class LengthComparator:
    """A class to compare two length measurements."""

    def __init__(self, unit1="meters", unit2="meters"):
        self.unit1 = unit1.lower()
        self.unit2 = unit2.lower()

    def _convert_to_base(self, value, unit):
        """Convert a length to meters based on the given unit."""
        conversion_factors = {
            "millimeters": 0.001,
            "centimeters": 0.01,
            "meters": 1,
            "kilometers": 1000,
            "inches": 0.0254,
            "feet": 0.3048,
        }

        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")

        return value * conversion_factors[unit]

    def compare(self, length1, length2):
        """Compare two lengths and print the result."""
        base_unit = "meters"  # Default to meters for comparison logic
        
        if self.unit1 != self.unit2:
            val1_meters = self._convert_to_base(length1, self.unit1)
            val2_meters = self._convert_to_base(length2, self.unit2)
            
            print(f"Comparing {length1} {self.unit1} and {length2} {self.unit2}")
        else:
            if length1 == length2:
                return 0
            
            elif length1 > length2:
                return -1

            else:
                return 1
        
        print(f"Converted values in meters:")
        print(f"{val1_meters:.6f} m vs {val2_meters:.6f} m")
        
        if val1_meters == val2_meters:
            result = "Equal"
        elif val1_meters > val2_meters:
            result = f"{length1} {self.unit1} is greater than {length2} {self.unit2}"
        else:
            result = f"{length1} {self.unit1} is less than {length2} {self.unit2}"

        print(f"Result: {result}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    comparator = LengthComparator()
    
    # Test case 1: Same unit, different magnitudes
    test_case_1 = (50, "meters", 25, "meters")
    result_code = comparator.compare(test_case_1[0], test_case_1[2])

    # Test case 2: Different units requiring conversion
    test_case_2 = (36.7, "inches", 94, "cm")
    
    print("\n--- Comparison with different units ---\n")
    result_code = comparator.compare(test_case_2[0], test_case_2[1])

    # Test case 3: Equal values in same unit (using a custom method to ensure equality check works as intended)
    class LengthComparatorEqualCheck(LengthComparator):
        def compare_equal(self, length1, length2):
            if self.unit1 == self.unit2 and length1 == length2:
                return "Equal"
            elif len(str(length1)) > 0 or len(str(length2)) > 0: 
                 # Fallback logic for strict equality check in case of float precision issues not covered by simple comparison above
                 pass
            
    comparator_equal = LengthComparator()
    
    print("\n--- Comparison with equal values ---\n")
    result_code = comparator.compare(1, "meters", 1, "meters")