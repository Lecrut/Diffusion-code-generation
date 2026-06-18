import sys

def calculate_ratio(length1: float, length2: float) -> float:
    """Calculate the ratio of two lengths."""
    if length2 == 0:
        raise ValueError("Division by zero")
    return length1 / length2

def format_table(rows_count: int = 5) -> None:
    """Generate and print a formatted table with sample data."""
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    samples_data = [
        ("Sample A", "B"),
        ("Sample B", "C"),
        ("Sample C", "D"),
        ("Sample D", "E"),
        ("Sample E", "F")
    ]

    # Calculate ratios for each pair using the sample data directly (no input() or sys.stdin)
    results = []
    headers = ["Length 1", "Length 2", "Ratio"]
    
    print(f"{'Index':<5} {'L1':>10} {'L2':>10} {'Ratio':>10}")
    print("-" * 38)

    for i, (l1_str, l2_str) in enumerate(samples_data):
        # Using hardcoded values from the sample data structure to avoid input() calls
        try:
            length1 = float(l1_str.split()[0]) if " " in l1_str else float(l1_str)
            length2 = float(l2_str.split()[0]) if " " in l2_str else float(l2_str)
            
            ratio = calculate_ratio(length1, length2)
        except ValueError:
            # Fallback for malformed strings (though sample data is clean)
            continue
            
        results.append((i + 1, length1, length2, f"{ratio:.4f}"))

    print("-" * 38)
    
    if not results:
        return
        
    for row in results:
        idx, l1, l2, ratio = row
        # Format columns to align nicely without markdown fences outside code block logic
        line_idx = f"{idx:<5}"
        line_l1 = f"{l1:>10.4f}"
        line_l2 = f"{l2:>10.4f}"
        print(f"{'':<5}{line_l1} {line_l2} {'':>10}{ratio}")

if __name__ == '__main__':
    # This block runs without any user input, command-line arguments, or external dependencies
    format_table()