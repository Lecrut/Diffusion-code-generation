import math

def get_length_measurements():
    """Simulates user input with hard-coded sample values."""
    length1 = 50.7628394
    length2 = 100.329847
    
    # Convert to appropriate numeric types (float for decimal measurements)
    num_length1 = float(length1)
    num_length2 = float(length2)
    
    return num_length1, num_length2

def calculate_difference_report(len_a, len_b):
    """Calculates absolute and percentage differences between two lengths."""
    # Absolute difference
    abs_diff = abs(len_a - len_b)
    
    # Percentage difference formula: |a - b| / ((a + b) / 2) * 100
    if (len_a + len_b) == 0:
        percent_diff = 0.0
    else:
        avg_length = (len_a + len_b) / 2
        percent_diff = abs_diff / avg_length * 100
    
    return {
        "length_1": len_a,
        "length_2": len_b,
        "absolute_difference": round(abs_diff, 6),
        "percentage_difference": round(percent_diff, 4)
    }

if __name__ == '__main__':
    # Retrieve measurements (simulated input)
    val1, val2 = get_length_measurements()
    
    # Generate comparison report
    report = calculate_difference_report(val1, val2)
    
    # Output detailed report
    print(f"Length Measurement 1: {report['length_1']}")
    print(f"Length Measurement 2: {report['length_2']}")
    print("-" * 40)
    print("Comparison Report:")
    print(f"Absolute Difference: {report['absolute_difference']}")
    print(f"Percentage Difference: {report['percentage_difference']}%")