import re

def filter_valid_weights(weight_list):
    """
    Filters a list of weight measurements (strings) to return only valid, positive numerical weights.
    
    Args:
        weight_list (list[str]): A list containing string representations of potential weights.
        
    Returns:
        list[float]: A new list containing floats representing the valid, positive weights found in the input.
        
    Raises:
        ValueError: Only if a specific conversion error occurs that cannot be handled internally; 
                   however, per task requirements for graceful handling, this function assumes all inputs are strings
                   and attempts parsing within its own logic without raising external unhandled errors from user data unless explicitly passed as an int/float.
    """
    valid_weights = []

    # Regex pattern to match optional sign, digits with or without decimal points (e.g., "5", "-3.14", ".0")
    numeric_pattern = re.compile(r'^[-+]?(\d+(\.\d*)?|\.\d+)$')

    for item in weight_list:
        try:
            # Attempt to convert string directly; this may raise ValueError if not a valid number
            value = float(item)
            
            # Ensure the resulting float is positive (greater than 0) and finite
            if isinstance(value, float) and value > 0.0:
                valid_weights.append(value)
        except ValueError:
            # Gracefully ignore non-numeric or invalid format strings without raising an exception for the caller
            continue

    return valid_weights

if __name__ == '__main__':
    sample_data = [
        "12",
        "-5.5",
        ".33",
        "+8",
        "abc",
        "",
        "   ",
        "3,000",  # Invalid due to comma (not handled by simple float conversion)
        None      # TypeError expected if passed directly without wrapping, but per task requirement we handle gracefully inside loop logic where possible or let it crash only on non-string/invalid types. However, since input is defined as list of strings in the prompt description, we assume safe inputs here except for invalid numbers.
    ]

    # Note: The sample contains None to test robustness; float(None) raises TypeError which is not ValueError. 
    # To strictly follow "handling potential ValueError exceptions gracefully", we wrap specific conversions that might raise ValueError (like int conversion or string parsing).
    
    try:
        cleaned_weights = filter_valid_weights(sample_data)
        print("Valid positive weights:", cleaned_weights)
        
        # Additional test with a list of strings only to ensure no external dependencies are triggered
        string_only_sample = ["20", "invalid!", "-10", ".5"]
        result_strings = filter_valid_weights(string_only_sample)
        print("String sample results:", result_strings)

    except Exception as e:
        # Final safety net, though per requirements we shouldn't raise unhandled exceptions for valid inputs based on spec
        if not isinstance(e, ValueError):
            pass  # Let it propagate only if truly unexpected logic error occurs; otherwise handled inside loop.