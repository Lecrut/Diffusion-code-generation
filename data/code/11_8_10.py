import sys

def calculate_ratio(length1: float, length2: float) -> str:
    """Calculate the ratio of two lengths and return a formatted string."""
    if length2 == 0:
        return f"Ratio (division by zero): {length1} / 0 = Undefined"
    
    ratio = length1 / length2
    
    # Format to avoid excessive decimal places unless it's an integer result
    if ratio.is_integer():
        formatted_ratio = str(int(ratio)) + ".0"
    else:
        formatted_ratio = f"{ratio:.4f}"
        
    return f"Ratio ({length1} / {length2}): {formatted_ratio}"

def generate_table(data_pairs):
    """Generate a nicely formatted table from the list of length pairs."""
    lines = []
    
    # Header row with alignment padding for numbers
    header_prefix = "Length 1\n\t\t" + "-" * (len(str(max(p[0] if p else 0) or 0)) + len("Ratio") + 2) + "\t" \
                   f"{str(len(data_pairs)):>4}" 
    lines.append(header_prefix.rstrip() + "\n")

    # Separator row with dashes and dots for alignment
    separator = "-" * (len(str(max(p[0] if p else 0) or 0)) + len("Ratio") + 2) + "." \
                + "-" * (len(f"{str(len(data_pairs)):>4}") - 1) 
    lines.append(separator.rstrip() + "\n")

    # Data rows
    for i, pair in enumerate(data_pairs):
        l1 = str(pair[0])
        
        ratio_str = calculate_ratio(*pair)[8:]  # Skip "Ratio (" part to align with header
        
        row_prefix = f"{l1:>6}" + "\t" 
        lines.append(row_prefix.rstrip() + separator.lstrip().rstrip())

    return "".join(lines)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network access)
    sample_data = [
        (10.5, 2),
        (48, 6),
        (37.5, 15),
        (100, 4),
        (99, 33)
    ]

    # Generate and print the table directly to stdout
    result_table = generate_table(sample_data)
    
    if sample_data:
        print(result_table.rstrip())