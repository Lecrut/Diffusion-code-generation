import math

def convert_to_float(value):
    """Convert a numeric string to float."""
    return float(value) if isinstance(value, str) else value

def calculate_absolute_difference(val1, val2):
    """Calculate the absolute difference between two values."""
    return abs(val1 - val2)

def calculate_percentage_difference(base_value, other_value):
    """Calculate the percentage difference relative to the base value."""
    if base_value == 0:
        raise ValueError("Base value cannot be zero for percentage calculation.")
    return (abs(other_value - base_value) / abs(base_value)) * 100

def generate_report(val1, val2):
    """Generate a detailed comparison report including absolute and percentage differences."""
    diff = calculate_absolute_difference(val1, val2)
    
    # Determine which value is the "base" for percentage calculation. 
    # Convention: usually against the larger one or just first argument if specified.
    # Here we use val1 as base unless it's zero to avoid division by zero errors in specific contexts,
    # but standard practice often uses the reference unit (val2) or simply val1.
    # Let's calculate percentage of difference relative to val1 for consistency with input order.
    
    try:
        percent_diff = calculate_percentage_difference(val1, val2) if abs(val1) > 0 else float('inf')
    except ValueError as e:
        return f"Absolute Difference: {diff}\nPercentage Difference (relative to first value): N/A ({e})"

    report_lines = [
        "=== Length Comparison Report ===",
        "",
        f"Value A: {val1}",
        f"Value B: {val2}",
        "",
        f"Absolute Difference: |{val1} - {val2}| = {diff:.4f}",
        ""
    ]

    if percent_diff != float('inf'):
        report_lines.append(f"Percentage Difference (relative to Value A): {(percent_diff)}%")
    else:
        # If base is zero, calculate relative to the second value instead for meaningful output
        try:
            alt_percent = calculate_percentage_difference(val2, val1) if abs(val2) > 0 else float('inf')
            report_lines.append(f"Percentage Difference (relative to Value B): {alt_percent:.4f}%")
            
            # If both are zero or one is effectively zero relative to the other contextually meaningful calc fails? 
            # Just pick the non-zero base.
        except ValueError:
            pass

    return "\n".join(report_lines)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    measurement_a = 10.5
    measurement_b = "7.2"

    val1 = convert_to_float(measurement_a)
    val2 = convert_to_float(measurement_b)

    report = generate_report(val1, val2)
    print(report)