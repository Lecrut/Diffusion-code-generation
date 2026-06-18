import sys

def calculate_ratios(data):
    """
    Reads length data from a list of integers, calculates the ratio for each consecutive pair,
    and returns the results as a formatted table string.
    
    Args:
        data (list): List of integer lengths representing pairs.
        
    Returns:
        str: Formatted table containing input values and calculated ratios.
    """
    if len(data) < 2:
        return "Error: At least two numbers are required to calculate a ratio.\n"

    # Process data in chunks of 2 (pairs)
    results = []
    
    print(f"{'Input Value':<15} {'Ratio':<10}")
    print("-" * 30)
    
    for i in range(0, len(data), 2):
        if i + 1 >= len(data):
            # Handle odd number of inputs by treating the last one as a zero or skipping (choosing skip here to avoid division by logic issues unless explicit pair is given)
            break
            
        try:
            length_a = data[i]
            length_b = data[i+1]
            
            if length_b == 0:
                ratio_str = "Undefined"
            else:
                # Calculate ratio as float, handling potential floating point precision for display
                ratio = length_a / length_b
                ratio_str = f"{ratio:.2f}"
                
        except (ValueError, TypeError):
            results.append(f"[{length_a}, {length_b}]") if i+1 < len(data) else ""
            continue
            
        # Format the output row
        input_str = str(length_a) + " / " + str(length_b)
        rows.append(input_str + f"\t|   |  {ratio_str}")

    return "\n".join(rows)

if __name__ == '__main__':
    # Hard-coded sample values representing length pairs.
    # Format: [length1, length2], [length3, length4], ...
    # Sample data: (50, 10), (80, 40), (100, 25)
    
    raw_data = "50 10\n80 40\n100 25"
    
    # Parse the input string into a list of integers
    pairs_str_list = []
    for line in raw_data.strip().split('\n'):
        parts = [int(x) for x in line.split()]
        if len(parts) == 2:
            pairs_str_list.extend(parts)

    print(calculate_ratios(pairs_str_list))