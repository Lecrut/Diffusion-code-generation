class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Prints:
            A message describing whether the first is greater, less than, equal to, 
            or if they are NaN/Infinity compared to each other.
        """
        # Handle special float values like infinity and NaN explicitly for clarity
        import math
        
        def get_type_name(val):
            return type(val).__name__

        t1_str = f"{temp1}"
        t2_str = f"{temp2}"

        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            print(f"Error: Both inputs must be numeric. Got {get_type_name(temp1)} and {get_type_name(temp2)}.")
            return

        # Check for NaN specifically as it behaves oddly in comparisons
        if math.isnan(float(temp1)) or math.isnan(float(temp2)):
            if math.isnan(float(temp1)) and math.isnan(float(temp2)):
                print(f"Both temperatures are NaN: {t1_str} vs {t2_str}")
            elif math.isnan(float(temp1)):
                print(f"{temp1} is undefined (NaN) compared to {temp2}.")
            else:
                print(f"{temp2} is defined while {temp1} is undefined (NaN).")
            return

        # Check for Infinity
        if math.isinf(float(temp1)) or math.isinf(float(temp2)):
            inf_val = float('inf')
            neg_inf_val = float('-inf')
            
            t1_is_pos_inf = temp1 == inf_val
            t1_is_neg_inf = temp1 == neg_inf_val
            
            t2_is_pos_inf = temp2 == inf_val
            t2_is_neg_inf = temp2 == neg_inf_val

            if t1_is_pos_inf and t2_is_pos_inf:
                print(f"Both temperatures are positive infinity.")
            elif t1_is_neg_inf and t2_is_neg_inf:
                print(f"Both temperatures are negative infinity.")
            elif t1_is_pos_inf and not (t2_is_pos_inf or t2_is_neg_inf):
                # Since we handled both inf cases above, this implies t2 is finite but smaller than +inf
                print(f"{temp1} is positive infinity which is greater than {temp2}.")
            elif t2_is_pos_inf and not (t1_is_pos_inf or t1_is_neg_inf):
                # Similar logic for the reverse case handled by standard comparison below, 
                # but explicit check here to avoid ambiguity if needed. Standard < handles this correctly though.
                pass 
            
        else:
            result = temp1 > temp2
            
            if result:
                print(f"{temp1} is greater than {temp2}.")
            elif temp2 > temp1:
                print(f"{temp2} is greater than {temp1}.")
            else:
                print(f"Both temperatures are equal to each other.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no network)
    
    tc = TemperatureComparator()

    # Test Case 1: Normal integers
    print("--- Sample 1 ---")
    tc.compare(25.0, 30.0)

    # Test Case 2: Floats where first is smaller
    print("\n--- Sample 2 ---")
    tc.compare(-5.5, -2.0)

    # Test Case 3: Equal values
    print("\n--- Sample 3 ---")
    tc.compare(100, 100)

    # Test Case 4: Positive Infinity vs Normal number
    import math
    try:
        tc.compare(float('inf'), 25.0)
    except OverflowError:
        print("Overflow occurred during comparison.")

    # Test Case 5: Negative Infinity vs Number
    try:
        tc.compare(float('-inf'), -10.0)
    except OverflowError:
        print("Overflow occurred during comparison.")

    # Test Case 6: NaN handling (if supported by environment, though math.isnan is used in logic)
    import sys
    if hasattr(math, 'isnan'):
        try:
            tc.compare(float('nan'), float('-inf'))
        except Exception as e:
            print(f"NaN comparison error occurred: {e}")

    # Test Case 7: Error handling for non-numeric input (simulated)
    print("\n--- Sample 7 ---")
    try:
        tc.compare("cold", "hot")
    except TypeError as e:
        print(f"Expected type error caught: {e}")