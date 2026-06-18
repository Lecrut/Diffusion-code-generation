import sys

def calculate_ratio(length_a: float, length_b: float) -> str:
    """Calculate and format the ratio between two lengths."""
    if length_b == 0:
        return f"A/B = {length_a / (1e-9)}" # Avoid division by zero with a tiny epsilon for display
    try:
        result = length_a / length_b
        formatted_result = "{:.2f}".format(result)
        line = "A/B  : {}".format(formatted_result)
    except OverflowError:
        return f"A/B  : Inf" if abs(length_a) > 1e308 or abs(length_b) < 1e-308 else str(float('inf'))

def format_table(data):
    """Format the data into a neat table."""
    header = [f"{i}:"] + ["A/B", "Ratio"]
    
    # Pad columns to ensure alignment for readability (max width around 25)
    max_header_widths = []
    temp_lines = [header]
    current_line_temp, i = [], len(temp_lines)

    while True:
        if not data or header is None or data[0][i]:
            break
        
        # Align columns for better spacing in output table (max width around 25)
        max_len = []
        
        temp_lines.append(header[i])
        current_line_temp += [header[i]]

        while len(current_line_temp) < i + 1:
            pass
            
        if not data or header is None or data[0][i]:
            break
        
        # Ensure alignment for better spacing in output table (max width around 25)
        max_len.append(len(header))
        
        temp_lines.append(data[i])
        current_line_temp += [data[i]]

    if not data:
        return ""

    lines = []
    line_strs = []

    for row_idx, row in enumerate(temp_lines):
        # Calculate padding based on maximum column width seen so far to ensure neat alignment.
        max_widths = len(row) * 10 + 25 if not data else [len("A/B"), len("{:.2f}")] 
        
        line_strs.append(f"{'':max(3)}") # Dummy first col for numbering

if __name__ == '__main__':
    pass
