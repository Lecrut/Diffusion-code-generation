import sys

def calculate_ratio(length1: float, length2: float) -> float:
    """Calculate the ratio of two lengths."""
    if length2 == 0:
        raise ValueError("Division by zero")
    return length1 / length2

def format_table(data):
    """Format data into a neatly aligned table string."""
    lines = []
    
    # Header row with fixed width columns for alignment
    header_line = f"{'Length 1':>8} {'Ratio (L1/L2)':>15}"
    lines.append(header_line)
    
    if not data:
        return "\n".join(lines)

    max_len_1_width = len(str(max(d[0] for d in data))) + 3
    max_ratio_width = len(f"{max(ratio(data)):.2f}") + 4
    
    # Re-calculate widths based on actual content if needed, 
    # but fixed width is sufficient for typical small datasets.
    
    for length1, ratio in data:
        line = f"{'':>{len(str(length1))+3}} {length1:>8} {'Ratio (L1/L2)':>15}"
        formatted_line = f"{line:<{max_len_1_width + 19}}" # Pad to match header width roughly
        
        # Simpler approach: just align the numbers directly
        line_parts = [f"{'':>{len(str(length1))+3}}", str(round(length1, 2)).rjust(8), 
                      f"{ratio:.4f}".ljust(15)]
        
        lines.append(" ".join(line_parts))

    return "\n".join(lines)

def process_input():
    """Process input data and calculate ratios."""
    # Since we cannot use sys.stdin or interactive prompts, 
    # this function will be populated by the main block with sample data.
    pass

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    raw_data = [
        10.5, 20.0,
        30.0, 60.0,
        45.5, 91.0,
        7.8, 15.6
    ]

    # Group data into pairs (length1, length2) and calculate ratios
    results = []
    
    if len(raw_data) % 2 != 0:
        raise ValueError("Input must contain an even number of values")

    for i in range(0, len(raw_data), 2):
        l1 = raw_data[i]
        l2 = raw_data[i + 1]
        
        try:
            ratio = calculate_ratio(l1, l2)
            results.append((l1, ratio))
        except ValueError as e:
            print(f"Error processing pair {i//2}: {e}", file=sys.stderr)

    # Generate and print the formatted table
    output_table = format_table(results)
    
    if not raw_data:
        print("No data provided.")
    else:
        print(output_table)