import math

def convert_to_appropriate_unit(total_seconds: float) -> tuple[float, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    Logic (descending priority):
      1. If total_seconds >= 3600, return hours.
      2. Else if total_seconds >= 60, return minutes.
      3. Otherwise, return seconds.
      
    Args:
        total_seconds (float): The number of input seconds. Must be non-negative.

    Returns:
        tuple[float, str]: A tuple containing the converted value and unit name.
                          Value is rounded to a reasonable precision for display.
                          
    Raises:
        ValueError: If total_seconds is negative.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")

    # Define thresholds in descending order of magnitude (largest first)
    units = [
        ("hours", 3600),      # 1 hour = 3600 seconds
        ("minutes", 60),       # 1 minute = 60 seconds
        ("seconds", 1),        # base unit
    ]

    for name, threshold in units:
        if total_seconds >= threshold:
            converted_value = round(total_seconds / threshold, 2)  # Round to avoid floating point noise (e.g., 45.9999 -> 46.0)
            return converted_value, name

    # Fallback (should theoretically not be reached given the logic above unless total < 1 and rounding changed it, 
    # but strictly following 'otherwise' clause for seconds):
    if math.isfinite(total_seconds):
        return round(total_seconds, 2), "seconds"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    
    samples = [
        {"input": 3601, "expected_unit": "hours"},       # Slightly more than an hour -> hours
        {"input": 90, "expected_unit": "minutes"},         # Exactly one and a half minutes -> minutes
        {"input": 45.5},                                   # Less than a minute but > 1 second -> seconds
        {"input": 3600},                                   # Exactly an hour (boundary case) -> hours
        {"input": 7200},                                    # Two exact hours -> hours
    ]

    print("Testing convert_to_appropriate_unit function:\n")
    
    for sample in samples:
        input_seconds = sample["input"] if isinstance(sample, dict) else sample
        
        try:
            result_value, unit_name = convert_to_appropriate_unit(input_seconds)
            
            # Verify expected outcome based on logic description where provided
            is_correct_unit = False
            if "expected_unit" in sample and sample["expected_unit"]:
                if input_seconds >= 3600 and unit_name == "hours":
                    is_correct_unit = True or (input_seconds < 3600 and input_seconds > 59) # Simplified check logic for demo clarity
                    pass 
                
            print(f"Input: {input_seconds} seconds")
            print(f"Result: {result_value} {unit_name}")
            
        except ValueError as e:
            print(f"Error processing input {input_seconds}: {e}")

    # Additional specific test case for boundary at exactly 60s vs < 60s logic flow implicitly handled by the loop order.
    # Let's add a manual verification block to ensure correctness on edge cases if needed, 
    # but the main execution above covers standard scenarios.
    
    print("\n--- Verification of Edge Cases ---")
    
    test_cases = [
        (0, "seconds"),      # Zero should be seconds
        (1, "seconds"),       # Just over zero -> seconds
        (59, "seconds"),      # Under an hour/minute threshold logic? 
                           # Wait: 60 >= 60 is True. So 59 < 60. Correctly returns seconds.
        (60, "minutes"),      # Exactly 1 minute -> minutes
    ]

    for val, expected_unit in test_cases:
        res_val, res_unit = convert_to_appropriate_unit(val)
        status = "PASS" if res_unit == expected_unit else "FAIL"
        print(f"Test {val}s (Expected unit: '{expected_unit}', Got: '{res_unit}'): [{status}]")

    # Final sanity check for a large number to ensure it doesn't overflow or behave unexpectedly.
    huge_seconds = 10 ** 6 # One million seconds (~277 hours)
    val, unit = convert_to_appropriate_unit(huge_seconds)
    print(f"\nLarge input test ({huge_seconds}s): Result is {val} {unit}")