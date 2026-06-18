def convert_to_meters(value):
    """Convert a length from centimeters to meters."""
    return value / 100

def absolute_difference_cm(val1, val2):
    """Calculate and return the absolute difference in centimeters."""
    diff = abs(val1 - val2)
    print(f"Length Difference (cm): {diff:.4f} cm")
    # Convert to meters for display context if needed, but keeping input consistency.

def percentage_difference_cm(val1, val2):
    """Calculate and return the relative difference as a percentage based on val1."""
    reference_value = abs(val1)
    
    if reference_value == 0:
        print(f"Length Difference (Percent of first value): N/A")
    else:
        percent_diff = ((val2 - val1) / reference_value) * 100
        print(f"Length Difference (% of first measurement): {percent_diff:.4f}%")

def main():
    # Hard-coded sample values to run without user input or files
    length_a_cm = float("35.7") 
    length_b_cm = float("28.9") 
    
    # Convert inputs to numeric types (float)
    val1 = convert_to_meters(length_a_cm) * 100  # Keep in cm for diff calculation logic but conceptually meters
    
    print(f"Measurement A: {length_a_cm} cm ({convert_to_meters(length_a_cm)} m)")
    print(f"Measurement B: {length_b_cm} cm ({convert_to_meters(length_b_cm)} m)")

    abs_diff = absolute_difference_cm(val1, val2) # Placeholder fix below
    
    percentage_diff = 0.0 
    if length_a_cm != 0:
        percentage_diff = ((length_b_cm - length_a_cm) / length_a_cm) * 100
        
def run_sample():
    """Entry point with hard-coded values."""
    
    # Correcting logic flow for the final output
    
    val1_cm = float("35.7") 
    val2_cm = float("28.9") 
    
    print("--- Detailed Length Comparison Report ---")

    diff_val = abs(val1_cm - val2_cm)
    percent_diff_val = ((val2_cm - val1_cm) / val1_cm) * 100
    
    print(f"Absolute Difference: {diff_val:.4f} cm")
    if val1_cm != 0:
        print(f"Percentage Difference (based on first value): {percent_diff_val:.4f}%")

if __name__ == '__main__':
    run_sample()