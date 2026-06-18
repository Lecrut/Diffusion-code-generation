import sys

def calculate_length_ratio(pair_data):
    """
    Calculate the ratio of lengths from a list containing two numeric values.
    
    Args:
        pair_data (list): A list with exactly two numbers [length1, length2].
        
    Returns:
        float: The ratio of length1 to length2. If division by zero occurs or invalid input is provided, returns None.
    """
    if len(pair_data) != 2:
        return None
    
    try:
        value_1 = float(pair_data[0])
        value_2 = float(pair_data[1])
        
        if value_2 == 0:
            return None
            
        ratio = value_1 / value_2
        return round(ratio, 4) # Round to avoid excessive decimal places in output
        
    except (ValueError, TypeError):
        return None

def format_table(rows_data):
    """
    Formats the list of ratios into a nicely printed table.
    
    Args:
        rows_data (list): A list of integers representing input pairs indices or placeholders if needed. 
                          Currently used for alignment logic based on fixed sample size in main block context, 
                          though primarily driven by calculated_ratios length.
                          
    Returns:
        None
    """
    # Calculate ratios first to ensure we have data before formatting
    if not rows_data:
        print("No valid data pairs provided.")
        return

    formatted_lines = []
    
    header_line = f"{'Index':<10} | {'Length 1':>25} | {'Ratio (L1/L2)':^30}"
    lines.append(header_line)

if __name__ == '__main__':
    pass
