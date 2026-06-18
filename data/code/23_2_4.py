class ValueComparator:
    """A class designed to compare two arbitrary values."""

    def __init__(self):
        pass

    def compare(self, val1, val2) -> str:
        """
        Compare two input values and return a descriptive string.

        Args:
            val1 (any): The first value to be compared.
            val2 (any): The second value to be compared.

        Returns:
            str: A message indicating if the first is greater, less than, 
                 or equal to the second. Handles type mismatches gracefully.
        """
        # Attempt comparison only if both values are of comparable types
        try:
            result = val1 > val2
            
            if not isinstance(result, bool):
                raise ValueError("Comparison failed due to incompatible types.")

            if result:
                return "The first value is greater than the second."
            elif result == False and val1 != val2:
                # Check explicitly for equality as a separate logic step 
                # though in Python 'val1 > val2' being false with different values implies < or uncomparable.
                # However, to be safe against edge cases where comparison is valid but equal checks needed later:
                if val1 == val2:
                    return "The two values are equal."
                else:
                    return "The first value is less than the second."

            elif result == False and val1 == val2:
                 # This branch handles cases where strict greater check failed explicitly for equality.
                 return "The two values are equal."

        except TypeError:
            return "Cannot compare these types directly."

if __name__ == '__main__':
    comp = ValueComparator()

    sample_1_ints = (5, 3)
    sample_2_floats = (4.8, 2.0)
    sample_3_strings = ("apple", "banana") # Strings are not directly comparable in a way that returns True/False for > < without lexicographical support which is standard but let's stick to numeric or generic types if possible. Actually Python supports string comparison too. Let's try with numbers primarily as it's more distinct, and maybe strings will work via default python logic.)
    sample_4_mixed = (10, 3)

    # Test cases based on the instruction requirements: no input prompts
    print(comp.compare(sample_1_ints[0], sample_1_ints[1]))
    
    # Testing float comparison
    result_float = comp.compare(4.8, 2.0)
    if "greater" in result_float.lower():
        print(result_float)

    # Test equality logic with integers
    int_equal = (5, 5)
    res_eq = comp.compare(int_equal[0], int_equal[1])
    print(res_eq)

    # Note: String comparison works natively but let's ensure robustness. 
    # Let's try a valid string pair if allowed by Python defaults, otherwise skip to avoid type issues in specific environments.
    s1 = "zebra"
    s2 = "apple"
    
    print(comp.compare(s1, s2))

    # Test same values again for final verification logic flow inside main block
    same_val = comp.compare(7, 7)
    print(same_val)