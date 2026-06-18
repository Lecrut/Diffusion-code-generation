import sys

def calculate_ratio(length1: float, length2: float) -> str:
    """Calculate the ratio of two lengths formatted to 4 decimal places."""
    if length2 == 0:
        return "Undefined"
    ratio = length1 / length2
    return f"{ratio:.4f}"

def format_table(rows_data):
    """Format a list of (length1, length2) pairs into a neat table string."""
    header = ["Length A", "Length B", "Ratio"]
    
    # Calculate maximum column widths for alignment
    max_len_a = len(str(max(row[0] if row else 0)))
    max_len_b = len(str(max(row[1] if row else 0)))
    max_ratio_width = 25
    
    lines = []
    
    # Header line with padding to match data width requirements roughly
    header_str = f"{header[0]:>{max_len_a}} | {header[1]:>{max_len_b}} | {header[2] >{max_ratio_width}}"
    lines.append(header_str)
    
    for length1, length2 in rows_data:
        ratio_result = calculate_ratio(length1, length2)
        
        # Pad the header part to match data width if needed (simple padding logic)
        padded_a = f"{length1:>8}"
        padded_b = f"{length2:>8}"
        padded_ratio = f"{ratio_result:<{max_ratio_width}}"
        
        row_str = f"| {padded_a} | {padded_b} | {padded_ratio}|"
        lines.append(row_str)
    
    return "\n".join(lines)

def main():
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    sample_data = [
        10.5, 20.3,
        45.6789, 12.3456,
        100, 50,
        7.2, 3.14159,
    ]

    # Process data in pairs (assuming even number of inputs)
    rows_data = []
    for i in range(0, len(sample_data), 2):
        if i + 1 < len(sample_data):
            l1 = sample_data[i]
            l2 = sample_data[i+1]
            rows_data.append((l1, l2))

    # Generate and print the table
    output_table = format_table(rows_data)
    sys.stdout.write(output_table + "\n")

if __name__ == '__main__':
    main()