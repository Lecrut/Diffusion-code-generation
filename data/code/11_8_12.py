import sys

def calculate_ratio(pair_str):
    """Calculate the ratio of two numbers from a string."""
    try:
        a, b = map(float, pair_str.strip().split())
        if b == 0:
            return None  # Avoid division by zero
        return a / b
    except ValueError:
        return None

def format_table(results):
    """Format the results into a neat table."""
    lines = []
    
    # Header
    header = f"{'Pair':<10} | {'Ratio':>20}"
    separator = "-" * len(header)
    lines.append(header)
    lines.append(separator)

    for pair_str, ratio in results:
        if ratio is None:
            display_ratio = "Undefined (Div by 0)"
        else:
            # Format to avoid excessive decimals but maintain precision
            formatted_ratio = f"{ratio:.15f}" 
            display_ratio = str(formatted_ratio)

        lines.append(f"{pair_str:<10} | {display_ratio:>20}")

    return "\n".join(lines)

def main():
    """Main function to read input, calculate ratios, and print the table."""
    
    # Hard-coded sample values as per requirements (no user interaction needed)
    raw_data = [
        "1 3",
        "2.5 4",
        "-6 -9", 
        "0 0"   # Edge case: division by zero
    ]

    results = []
    
    for pair_str in raw_data:
        ratio = calculate_ratio(pair_str)
        if ratio is not None:
            results.append((pair_str, ratio))
        else:
            print(f"Warning: Could not process '{pair_str}'. Skipping.") # Log issue without halting

    output_table = format_table(results)
    
    # Ensure a newline at the very end of stdout for clean formatting
    if output_table and not output_table.endswith("\n"):
        output_table += "\n"

    print(output_table, end="")

if __name__ == '__main__':
    main()