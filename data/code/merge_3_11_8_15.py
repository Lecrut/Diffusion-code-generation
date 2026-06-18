import sys

def calculate_ratio(length_pair):
    """Calculate the ratio of two lengths."""
    if length_pair[0] <= 0:
        return None, "Length must be positive"
    
    try:
        first = float(length_pair[0])
        second = float(length_pair[1])
        
        if second == 0:
            return None, "Division by zero"
            
        ratio = first / second
        
        # Format to avoid floating point precision issues with trailing zeros unless needed
        formatted_ratio = f"{ratio:.6f}".rstrip('0').rstrip('.')
        
        return float(formatted_ratio), ""
    except ValueError:
        return None, "Invalid number format"

def parse_length_data(data):
    """Parse input data into pairs of lengths."""
    lines = [line.strip() for line in data if line.strip()]
    
    i = 0
    while i < len(lines) - 1:
        try:
            first_val, second_val = float(lines[i]), float(lines[i+1])
            
            # Check if inputs are valid positive numbers (allowing scientific notation like '1e2')
            if not isinstance(first_val, (int, float)) or not isinstance(second_val, (int, float)):
                yield None, "Invalid number format"
                
        except ValueError:
            yield lines[i], f"Error parsing line {i+1}: Expected numeric values separated by space/comma/newline"

            
def generate_table(lines):
    """Generate a formatted table of results."""
    
    # Initialize columns with headers
    output_lines = []
    output_lines.append("Index | First Length | Second Length | Ratio")
    output_lines.append("-" * 45)
    
    for idx, line in enumerate(lines):
        try:
            first_val, second_val = float(line.split()[0]), float(line.split()[1]) if ' ' in line else float(line), None
            
            # Handle comma or space separation logic more robustly
            parts = [p.strip() for p in str(line).split()]
            
            if len(parts) >= 2:
                first_val, second_val = float(parts[0]), float(parts[1])
                
                ratio_result, error_msg = calculate_ratio((first_val, second_val))
                
                if not isinstance(ratio_result, (int, float)):
                    output_lines.append(f"{idx} | {line[:25]}... | {second_val:.6f}" + (" " * 30) + f"| Error: {error_msg}")
                    
            else:
                # Fallback for single value or malformed input treated as error row
                ratio_result, error_msg = calculate_ratio((first_val, second_val)) if len(parts) == 1 and parts[0] in [''] else (None, "Missing pair")
                
        except ValueError:
            output_lines.append(f"{idx} | {line[:25]}... | -" + (" " * 37) + "| Error: Invalid input format")

    return '\n'.join(output_lines)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    
    # Simulating standard input content directly in memory
    
    raw_input_data = """10 5.0
20 4
3e-2 6e-2
100 1"""

    parsed_lines = [line.strip() for line in raw_input_data.split('\n') if line.strip()]
    
    # Processing and formatting the data into a table
    
    output_table = generate_table(parsed_lines)
    
    print(output_table)