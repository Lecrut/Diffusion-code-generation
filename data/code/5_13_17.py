def validate_numeric_input(value):
    """Check if a value is numeric."""
    try:
        float(value)
        return True, None
    except ValueError:
        return False, f"Invalid input '{value}'. Please enter a number."

def compare_measurements(length1_str, length2_str):
    """Compare two lengths and calculate the difference."""
    if not validate_numeric_input(length1_str)[0]:
        print(validate_numeric_input(length1_str)[1])
        return None
    
    if not validate_numeric_input(length2_str)[0]:
        print(validate_numeric_input(length2_str)[1])
        return None

    length1 = float(length1_str)
    length2 = float(length2_str)

    difference = length1 - length2

    comparison_text = (f"First measurement: {length1}\nSecond measurement: {length2}\nDifference: {difference}")
    
    print(comparison_text)
    return None

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes without user input.
    sample_length_1 = "5"
    sample_length_2 = "3"
    
    compare_measurements(sample_length_1, sample_length_2)