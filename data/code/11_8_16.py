import sys

def calculate_ratio(length_a: float, length_b: float) -> float:
    """Calculate the ratio of length a to length b."""
    if length_b == 0:
        raise ValueError("Division by zero")
    return length_a / length_b

def format_table(data: list[tuple[float, float]]) -> str:
    """Format the data into a neatly aligned table string."""
    lines = []
    
    # Header with column widths calculated from max values + padding
    if not data:
        return "No data provided."
        
    col1_max = len(str(max(d[0] for d in data)))
    col2_max = len(str(max(d[1] for d in data)))
    
    header = f"{'Length A':>{col1_max}} {'/' :<{col2_max+3}} {'Ratio':>8}"
    lines.append(header)
    
    # Separator line with dashes to match column widths
    separator = "-" * (col1_max + 4 + col2_max + 9)
    lines.append(separator)
    
    for a, b in data:
        ratio = calculate_ratio(a, b)
        formatted_a = f"{a:.6f}" if len(str(a)) > col1_max else str(a)
        # Ensure the '/' takes up enough space to align nicely with header length 4 chars
        slash_part = " /" + (" " * (col2_max - len(f"{b:.6f}"))) 
        formatted_b = f"{b:.6f}" if len(str(b)) > col2_max else str(b)
        
        line = f"{formatted_a:>8.4f}{slash_part:<{col2_max+3}} {ratio:>.10g}"
        lines.append(line)

    return "\n".join(lines)

def main():
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    raw_data = [
        "10.5 20.3",
        "5.0 10.0",
        "100.0 25.0",
        "7.89 4.32"
    ]

    # Parse the input data manually from strings to avoid any interactive prompts or sys.stdin calls
    pairs = []
    for line in raw_data:
        parts = [float(x.strip()) for x in line.split()]
        if len(parts) == 2:
            pairs.append((parts[0], parts[1]))

    # Generate and print the formatted table
    result_table = format_table(pairs)
    
    # Output only the table, no extra text outside the code block logic
    print(result_table)

if __name__ == '__main__':
    main()