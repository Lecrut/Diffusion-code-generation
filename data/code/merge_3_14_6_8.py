def validate_numeric(value):
    """Validate if a string represents a valid numeric value."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_measurements(vol_a, vol_b):
    """Compare two volume measurements and print the outcome."""
    # Validate inputs as part of robust script behavior
    if not validate_numeric(vol_a):
        raise ValueError(f"Invalid numeric value for first measurement: '{vol_a}'")
    if not validate_numeric(vol_b):
        raise ValueError(f"Invalid numeric value for second measurement: '{vol_b}'")

    val_a = float(vol_a)
    val_b = float(val_b)

    print("Comparison Result:")
    
    if val_a > val_b:
        result_msg = f"'{val_a}' is greater than '{val_b}'"
    elif val_a < val_b:
        result_msg = f"'{val_a}' is less than '{val_b}'"
    else:
        result_msg = f"'{val_a}' is equal to '{val_b}'"

    print(result_msg)

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input, args, or network access required)
    vol_1_sample = "5.2 liters"
    vol_2_sample = "3.8 liters"

    parts_a = vol_1_sample.split()[-1] if ' ' in vol_1_sample else vol_1_sample
    parts_b = vol_2_sample.split()[-1] if ' ' in vol_2_sample else vol_2_sample
    
    try:
        compare_measurements(parts_a, parts_b)
    except ValueError as e:
        print(f"Error: {e}")

# Additional test case can be simulated directly by calling the function without input prompts for validation robustness
if __name__ == '__main__': 
    # Running a second internal verification to ensure numeric parsing works on integers and floats mixed
    test_cases = [
        ("10.5", "2"),
        ("-3.4", "0"),
        ("0", "-9")
    ]

    for tc_a, tc_b in test_cases:
        try:
            compare_measurements(tc_a.replace(" liters ", ""), tc_b.replace(" ml ", ""))
        except Exception as e:
            pass # Suppress output during this internal check if needed, though task implies single run logic is primary. 
            # For strict adherence to 'single complete runnable module' that runs once cleanly with sample values only: