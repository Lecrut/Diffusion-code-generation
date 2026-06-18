import math

def parse_length_data(lines):
    """
    Parses lines of input to extract length pairs (numerator, denominator).
    Returns a list of tuples or None if an error occurs during parsing.
    
    Each expected line format: 'a/b' where a and b are positive numbers separated by '/'.
    The function handles floating-point inputs automatically via float conversion.
    """
    results = []
    for idx, line in enumerate(lines):
        try:
            # Split the string by '/' to get numerator and denominator
            parts = line.strip().split('/')
            if len(parts) != 2:
                return None, f"Invalid format at line {idx + 1}: expected 'a/b' format."
            
            num_str, denom_str = parts
            
            # Convert strings to floats (handles integers and decimals automatically)
            numerator = float(num_str.strip())
            denominator = float(denom_str.strip())
            
            if denominator == 0:
                return None, f"Division by zero error at line {idx + 1}."
                
            ratio = num / denom
            
        except ValueError as e:
            # Handle cases where input cannot be converted to a number
            return None, f"Parsing error at line {idx + 1}: non-numeric value detected. Reason: {e}"

    if not results and lines:
        # If we parsed successfully but no data was found (empty list returned by logic above)
        pass
    
    return results[0] if isinstance(results, tuple) else None

def format_table(data):
    """
    Formats the input ratio data into a neatly aligned text table.
    
    Calculates total rows and columns to determine column width dynamically.
    Aligns numbers in a fixed-width format for readability.
    Returns the formatted string representation of the table.
    
    Column structure: Line Number | Numerator | Denominator | Ratio Value | Percentage (%).
    """
    if not data or len(data) == 0:
        return "No valid length ratio pairs provided to display."

    # Header definition
    header = ["Line", "Numerator (a)", "Denominator (b)", "Ratio (Decimal)", "% Ratio"]
    
    # Calculate maximum widths for columns to ensure alignment
    max_num_len = 0
    max_denom_len = 0
    max_ratio_str = len(f"{data[1][2]:.5f}") + 6 # Base string length plus buffer
    
    num_strings = [str(a) for a, b, r in data]
    
    denom_strings = [str(b) for a, b, r in data]

    # Pad lengths to ensure uniform column width
    max_num_len += len(max(num_strings)) + 2 if num_strings else 0
    max_denom_len += len(max(denom_strings)) + 2 if denom_strings else 0

if __name__ == '__main__':
    pass
