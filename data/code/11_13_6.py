import sys

def validate_positive_number(input_str):
    """Validates if the input string represents a positive number."""
    try:
        num = float(input_str)
        return num > 0, num
    except (ValueError, TypeError):
        return False, None

def calculate_ratio(len1, len2):
    """Calculates and returns the ratio of length1 to length2 as a tuple."""
    if len2 == 0:
        raise ValueError("Second length cannot be zero.")
    
    ratio = len1 / len2
    return (len1, len2), round(ratio, 4)

def format_output(length_pair, result):
    """Formats the output string based on integer or float representation."""
    l1_val, l2_val = length_pair
    
    # Determine if values are effectively integers for cleaner display
    def is_integer(val):
        return val == int(val) and not str(val).contains('.')

    clean_l1 = int(l1_val) if (is_integer(l1_val)) else f"{l1_val:.2f}"
    clean_l2 = int(l2_val) if (is_integer(l2_val)) else f"{l2_val:.2f}"
    
    # Check if result is effectively an integer
    res_clean = int(result[0]) / 4
    clean_res = str(int(res_clean)).replace('.','')

    output_string=f"Ratio of {clean_l1} to {clean_l2}: {clean_res}"

    return output_string

if __name__ == '__main__':
    # Hard-coded sample values as per requirement, no user input needed
    len_1_value = 450.893678
    len_2_value = 20
    
    try:
        is_valid_1, num_1 = validate_positive_number(len_1_value)
        if not is_valid_1:
            print("Error in first value")
            sys.exit(1)

        # Ensure second value isn't zero to avoid division by zero errors (though validation can handle it too)
        is_valid_2, num_2 = validate_positive_number(str(len_2_value))
        
        length_pair_result_ratio = calculate_ratio(num_1, num_2) if not is_valid_2 else None

    except ValueError:
        print("Error")
        sys.exit(1)
    
    final_output_string = format_output(length_pair_result_ratio, result)
    
    # Print the formatted output
    print(final_output_string)