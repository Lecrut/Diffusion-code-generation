import sys

def get_positive_number(prompt):
    """Prompt user (or use default) to input a positive number."""
    # Since we cannot call interactive input() per constraints, 
    # this function is designed to be called with hard-coded values in the main block.
    return None  # Placeholder logic; actual usage will pass value directly

def calculate_ratio(length_a: float, length_b: float) -> tuple[float | int]:
    """Calculate and validate ratio between two lengths."""
    if not isinstance(length_a, (int, float)) or not isinstance(length_b, (int, float)):
        raise ValueError("Inputs must be numeric.")
    
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both inputs must be positive numbers.")

    ratio = length_a / length_b
    return ratio

def format_result(ratio: float) -> str:
    """Format the result in a clear manner."""
    # Determine significant digits based on input magnitude (simplified for this task)
    if 0.1 <= abs(length_a * length_b) < 1e6 and 0.1 <= ratio < 1e6:
        formatted_ratio = f"{ratio:.2f}"
    else:
        formatted_ratio = str(ratio)

    return (
        f"Ratio of {length_a} to {length_b}: "
        f"{formatted_ratio}\n"
        f"Simplified Fraction: {int(length_a)}:{int(length_b)}\n"
        f"(Note: Simplified fraction assumes integer inputs)"
    )

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, args, or network access is needed.
    length1 = 450.75
    length2 = 300

    try:
        ratio_value = calculate_ratio(length1, length2)
        
        if isinstance(ratio_value, float):
            result_string = format_result(ratio_value)
        else:
            # Fallback for integer division scenario (though Python / always returns float)
            result_string = f"Ratio of {length1} to {length2}: " + str(length1/length2)

        print(result_string.strip())
    except ValueError as e:
        print(f"Error: Invalid input - {e}", file=sys.stderr)