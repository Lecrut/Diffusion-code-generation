import sys

def calculate_ratio(length1: float, length2: float) -> float:
    """Calculate the ratio of two lengths."""
    if length2 == 0:
        return None
    return length1 / length2

def format_table(data):
    """Format data into a neat table string."""
    lines = []
    
    # Header
    header = f"{'Length 1':>15} {'Ratio (L1/L2)':<30}"
    lines.append(header)
    
    for length1, ratio in data:
        if ratio is None:
            formatted_ratio = "Undefined (division by zero)"
        else:
            # Format to avoid excessive floating point noise while keeping precision
            formatted_ratio = f"{ratio:.4f}"
        
        line = f"{length1:>15.2f} {formatted_ratio:<30}"
        lines.append(line)
    
    return "\n".join(lines)

def main():
    # Hard-coded sample values to satisfy the requirement of running without user input
    raw_input_data = [
        "10 2",      # Ratio: 5.0
        "34 7" ,     # Ratio: ~4.86
        "99 3" ,     # Ratio: 33.0
        "0 5"       # Ratio: Undefined (division by zero)
    ]

    results = []
    
    for line in raw_input_data:
        parts = list(map(float, line.split()))
        
        if len(parts) != 2:
            continue
            
        length1, length2 = parts[0], parts[1]
        ratio = calculate_ratio(length1, length2)
        results.append((length1, ratio))

    table_output = format_table(results)
    
    # Output the formatted result to standard output (stdout), not stdin or interactive prompts
    print(table_output)

if __name__ == '__main__':
    main()