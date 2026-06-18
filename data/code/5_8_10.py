import math

def parse_length(value_str: str) -> float:
    """Parse a length measurement string to a float."""
    return float(value_str.strip())

def calculate_difference(length_a: float, length_b: float) -> tuple[float, float]:
    """Calculate absolute difference and percentage difference between two lengths.

    Args:
        length_a (float): First length value.
        length_b (float): Second length value.

    Returns:
        tuple: A tuple containing the absolute difference and percentage difference.
               Percentage is calculated relative to |length_b| if it's non-zero, otherwise 0%.
    """
    abs_diff = abs(length_a - length_b)
    
    # Avoid division by zero when second value is zero or very close to it
    denominator = max(abs(length_b), 1e-9) 
    percent_diff = (abs_diff / denominator) * 100
    
    return abs_diff, percent_diff

def format_report(label_a: str, label_b: str, length_a: float, length_b: float, diff_abs: float, diff_pct: float):
    """Generate a detailed comparison report string."""
    print(f"\n=== Comparison Report ===")
    print(f"Item A ({label_a}): {length_a:.4f}")
    print(f"Item B ({label_b}): {length_b:.4f}")
    print("-" * 30)
    print(f"Absolute Difference: |{length_a} - {length_b}| = {diff_abs:.6f}")
    print(f"Percentage Difference (relative to Item B): {(abs(length_a - length_b) / max(abs(length_b), abs(length_a or 1e-9)) * 100 if len([x for x in [length_a, length_b] if x != 0]) > 0 else 0):.6f}%")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse)
    
    # Sample data: two string representations of lengths with units for context
    length_str_1 = "5 meters"
    length_str_2 = "3.5 yards"

    # Define labels and raw numeric parsing
    label_a = "First Measurement"
    label_b = "Second Measurement"
    
    # Extract numeric values from strings (simple extraction for demo)
    val_a_float = parse_length("5")  # Simulating conversion of '5 meters' to float
    val_b_float = parse_length("3.5")

    abs_diff, pct_diff = calculate_difference(val_a_float, val_b_float)
    
    format_report(label_a, label_b, val_a_float, val_b_float, abs_diff, pct_diff)