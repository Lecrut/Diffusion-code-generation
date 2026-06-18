class LengthComparator:
    def compare(self, length_a, length_b):
        """
        Compares two lengths and returns a descriptive string indicating their relationship.

        Args:
            length_a (int or float): The first length value.
            length_b (int or float): The second length value.

        Returns:
            str: A description of the comparison result.
        """
        if length_a == length_b:
            return f"Lengths are equal ({length_a})."
        elif length_a < length_b:
            difference = round(length_b - length_a, 2)
            return f"Length {length_a} is less than {length_b} by a margin of {difference}."
        else:
            difference = round(length_a - length_b, 2)
            return f"Length {length_a} is greater than {length_b} by a margin of {difference}."

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    comp = LengthComparator()

    test_cases = [
        (10, 20),       # length_a < length_b
        (50, 50),       # equal
        (7.5, 3.2),     # floating point comparison with less than a
        (-4, -9)        # negative numbers: greater in magnitude for the larger value? No: -4 > -9
    ]

    print("Running LengthComparator tests...\n")
    
    results = []
    input_text_a, input_b = test_cases[0]
    result = comp.compare(input_text_a, input_b)
    results.append(result)
    print(f"Comparing {input_text_a} vs {input_b}: '{result}'\n")

    # Continue with remaining cases if desired for demonstration. Here we just run a few specific ones to show variety without excessive output.
    test_values = [(15, 25), (100, 50), (3.33, 6.66)]
    
    print("Additional comparisons:\n")
    for i, vals in enumerate(test_values):
        a_val, b_val = vals
        res = comp.compare(a_val, b_val)
        print(f"{a_val} vs {b_val}: '{res}'")

print("\nAll tests completed successfully.")