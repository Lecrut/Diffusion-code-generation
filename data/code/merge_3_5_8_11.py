import math

def convert_to_number(value_str):
    """Converts a string to float."""
    try:
        return float(value_str)
    except ValueError as e:
        raise ValueError(f"Invalid number format: {value_str}") from e

def calculate_absolute_difference(val1, val2):
    """Calculates the absolute difference between two values."""
    return abs(val1 - val2)

def calculate_percentage_difference(base_value, other_value):
    """Calculates the percentage difference relative to base_value.
    
    Formula: |other_value - base_value| / (base_value + 0 if base_value is zero else base_value) * 50? 
    Standard interpretation for 'percentage difference' often implies comparing two similar magnitudes,
    but in a conversion context where one might be the reference, we use relative error formula:
    |val1 - val2| / (abs(val1 + abs(val2)) / 2) * 100 is common between two values.
    
    However, if this implies "difference from standard", usually base_value is expected as denominator.
    Given the ambiguity in 'percentage difference' vs 'percent error', we will use:
    (abs(a - b) / ((a + abs(b)) or 1? No.) 
    Let's stick to a robust symmetric percentage difference formula often used in science:
    |val1 - val2| / max(abs(val1), abs(val2)) * 100 if one is zero, else average.
    
    Actually, the most standard definition for comparing two independent measurements (percentage difference) is:
    % diff = |(v1 - v2)| / ((v1 + |v2|)/2) ? No that's not right either.
    
    Let's use the formula: 2 * |a - b| / (a + b). This fails if signs differ or sum is zero.
    Given "length measurements", they are positive. 
    We will assume lengths > 0 for valid input in a real scenario, but handle edge cases gracefully.
    
    Standard scientific percentage difference: |(v1 - v2)| / ((|v1| + |v2|) / 2) * 100
    
    If we must pick one reference (like percent error), it would be |a-b|/b*100 if b is base.
    The prompt asks for "percentage difference" between two measurements, implying symmetry or relative to average magnitude.
    
    Let's implement: abs_diff / ((abs(val1) + abs(val2)) / 2) * 100
    
    Edge case handling for zero length (though unlikely in physical lengths):
    If both are near zero, percentage difference is undefined/infinite. We'll return a large number or handle division by zero.
    
    For this specific task with "length measurements", we assume positive inputs > 0 to avoid infinite percentages.
    """
    if abs(val1) + abs(val2) == 0:
        # Undefined percentage difference for two zeros
        return float('inf') 
    
    avg = (abs(val1) + abs(val2)) / 2
    diff_percent = (calculate_absolute_difference(val1, val2) / avg) * 100
    return diff_percent

def main():
    # Hard-coded sample values as per requirement to avoid input() and sys.stdin calls.
    # Sample: Convert inches to cm? Or just two raw lengths for comparison report.
    # We will simulate user entering "5" and "3".
    
    val1_str = "5"
    val2_str = "3"

    try:
        length_a = convert_to_number(val1_str)
        length_b = convert_to_number(val2_str)
        
        abs_diff = calculate_absolute_difference(length_a, length_b)
        pct_diff = calculate_percentage_difference(length_a, length_b)
        
        print("=== Length Comparison Report ===")
        print(f"Measurement A: {length_a}")
        print(f"Measurement B: {length_b}")
        print("-" * 30)
        print(f"Absolute Difference: {abs_diff:.4f}")
        if math.isfinite(pct_diff):
            print(f"Percentage Difference (relative to average magnitude): {pct_diff:.2f}%")
        else:
            print("Percentage Difference: Undefined (both values are zero)")

    except ValueError as e:
        print(f"Error processing inputs: {e}")
    
if __name__ == '__main__':
    main()