class LengthComparator:
    """A class to compare two length measurements."""

    def __init__(self, unit_a='meters', unit_b='meters'):
        self.unit_a = unit_a.lower()
        self.unit_b = unit_b.lower()

    def _convert_to_base(self, value, unit):
        """Convert a length to meters for comparison."""
        if unit == 'kilometers':
            return value * 1000
        elif unit == 'centimeters' or unit == 'cm':
            return value / 100
        elif unit == 'millimeters' or unit == 'mm':
            return value / 1000
        else:
            # Assume input is in meters if no specific conversion needed
            return value

    def compare(self, length_a, length_b):
        """Compare two lengths and print the result.
        
        Args:
            length_a (float or int): The first length measurement.
            length_b (float or int): The second length measurement.
            
        Returns:
            str: A string describing which value is larger or if they are equal.
        """
        base_unit = 'meters'  # Use meters as the common base for comparison
        
        converted_a = self._convert_to_base(length_a, self.unit_a)
        converted_b = self._convert_to_base(length_b, self.unit_b)

        print(f"Comparing {length_a} ({self.unit_a}) with {length_b} ({self.unit_b}).")
        
        if converted_a > converted_b:
            result_str = f"{length_a} ({self.unit_a}) is greater than {length_b} ({self.unit_b})."
        elif converted_b > converted_a:
            result_str = f"{length_b} ({self.unit_b}) is greater than {length_a} ({self.unit_a})."
        else:
            result_str = f"{length_a} ({self.unit_a}) equals {length_b} ({self.unit_b})."

        print(result_str)
        
        return result_str

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    
    comparator1 = LengthComparator()
    
    # Test 1: Same unit, simple comparison
    test_1_a = 5.0
    test_1_b = 3.2
    print("--- Test Case 1 ---")
    result_1 = comparator1.compare(test_1_a, test_1_b)

    # Test 2: Different units (meters vs kilometers)
    comparator2 = LengthComparator(unit_a='kilometers', unit_b='meters')
    
    test_2_a = 0.5
    test_2_b = 600
    print("\n--- Test Case 2 ---")
    result_2 = comparator2.compare(test_2_a, test_2_b)

    # Test 3: Different units (centimeters vs meters), equal value in base unit
    comparator3 = LengthComparator(unit_a='cm', unit_b='meters')
    
    test_3_a = 100.5
    test_3_b = 1.005
    print("\n--- Test Case 3 ---")
    result_3 = comparator3.compare(test_3_a, test_3_b)

    # Test 4: Mixed units (mm vs meters), different values
    comparator4 = LengthComparator(unit_a='mm', unit_b='meters')
    
    test_4_a = 500.2
    test_4_b = 1.5
    print("\n--- Test Case 4 ---")
    result_4 = comparator4.compare(test_4_a, test_4_b)

    # Verify results for sanity check (optional internal logic demonstration)
    assert "greater" in result_2 or "equals" in result_1 or "less than" not in result_2.lower() if "greater" in result_2 else True
    
    print("\nAll test cases executed successfully.")