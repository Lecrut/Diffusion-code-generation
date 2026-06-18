class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperature values and prints a descriptive string indicating their relationship.

        Args:
            temp1 (float or int): The first temperature value.
            temp2 (float or int): The second temperature value.
        
        Prints:
            A message describing whether the temperatures are equal, temp1 is higher/lower than temp2.
        """
        if temp1 == temp2:
            print(f"Both temperatures are equal: {temp1}")
        elif temp1 > temp2:
            diff = temp1 - temp2
            unit_suffix = "°C"  # Assuming Celsius for generality, but the logic holds for any temperature scale with a difference
            if isinstance(temp1, float):
                formatted_diff = f"{diff:.4f}"
            else:
                formatted_diff = str(diff)
            print(f"The first temperature is higher by {formatted_diff} units ({temp1} vs {temp2})")
        else:
            diff = temp2 - temp1
            if isinstance(temp1, float):
                formatted_diff = f"{diff:.4f}"
            else:
                formatted_diff = str(diff)
            print(f"The second temperature is higher by {formatted_diff} units ({temp1} vs {temp2})")

if __name__ == '__main__':
    comparator = TemperatureComparator()

    # Sample values to test the comparison logic without user input or external dependencies
    
    # Test 1: Equal temperatures
    print("--- Test Case 1 (Equal) ---")
    temp_a, temp_b = 25.0, 25.0
    comparator.compare(temp_a, temp_b)

    # Test 2: First temperature is higher by a whole number
    print("\n--- Test Case 2 (First Higher - Integer Diff) ---")
    temp_c, temp_d = 30, 18
    comparator.compare(temp_c, temp_d)

    # Test 3: Second temperature is slightly lower with decimal precision
    print("\n--- Test Case 3 (Second Lower - Decimal Difference) ---")
    temp_e, temp_f = -5.7249, -5.7001
    comparator.compare(temp_e, temp_f)

    # Test 4: First temperature is higher by a very small amount
    print("\n--- Test Case 4 (First Higher - Tiny Difference) ---")
    temp_g, temp_h = 20.105, 20.106
    comparator.compare(temp_g, temp_h)

    # Test 5: First temperature is negative and second is positive
    print("\n--- Test Case 5 (Signs Different - Second Higher) ---")
    temp_i, temp_j = -10.0, 10.0
    comparator.compare(temp_i, temp_j)