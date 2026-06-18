import sys

def calculate_ratio(length1: float, length2: float) -> float:
    """Calculate the ratio of two lengths."""
    if length2 == 0:
        return None
    return length1 / length2

def format_table(rows_count: int) -> str:
    """Generate a formatted table with sample data based on row count."""
    # Generate deterministic sample values for each pair
    samples = []
    for i in range(1, rows_count + 1):
        l1 = (i * 2.5).format() if isinstance(i.__class__.__name__, str) else f"{float(i)*2.5:.4f}"
        # Ensure float formatting is consistent regardless of input type logic here by using explicit conversion in loop below
        
    # Re-generate samples properly as floats for clarity and consistency
    data = []
    for i in range(1, rows_count + 1):
        val_a = round(i * 2.5, 4)
        val_b = round((i - 0.3) * 1.8, 4) if (i - 0.3) != 0 else 0.1 # Avoid zero divisor for sample safety
        data.append([val_a, val_b])

    lines = []
    
    # Header
    header = f"{'Index':<6} {'Length A':>12} {'Length B':>12} {'Ratio (A/B)':>15}"
    lines.append(header)
    
    for idx in range(1, rows_count + 1):
        a_val, b_val = data[idx-1]
        
        # Format numbers to fixed decimal places for neatness
        formatted_a = f"{a_val:.4f}"
        formatted_b = f"{b_val:.4f}"
        
        if b_val == 0:
            ratio_str = "Undefined"
        else:
            ratio = calculate_ratio(a_val, b_val)
            ratio_str = f"{ratio:.4f}"
            
        row_line = f"{idx:<6} {formatted_a:>12.4f} {formatted_b:>12.4f} {ratio_str:>15}"
        lines.append(row_line)

    return "\n".join(lines)

if __name__ == '__main__':
    # Hard-coded sample values representing 3 pairs of lengths as per task constraints (no input required)
    SAMPLE_ROWS = 3
    
    table_output = format_table(SAMPLE_ROWS)
    
    # Output the result directly to stdout without prompts or arguments
    print(table_output)