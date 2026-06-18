import sys

def parse_and_convert(line):
    """Parses a temperature value and unit from string and converts to Kelvin."""
    line = line.strip()
    if not line:
        return None
    
    parts = line.split(None, 1) # Split into base temp and optional unit
    try:
        temp_value = float(parts[0])
        
        default_unit = 'C'
        if len(parts) > 1:
            unit_str = parts[1].upper()
            
            if unit_str == 'F':
                default_unit = 'F'
            elif unit_str in ('K', 'CELSIUS'):
                pass # Celsius is the assumed base for conversion to Kelvin anyway, but good flag
            
        else:
            # Assume Celsius by default based on problem context usually implying C/F input or just number implies C
            default_unit = 'C'

        if temp_value == float('inf') or temp_value == float('-inf'):
            return None
        
        conversion_factor = 0.0
        offset = 273.15
        
        # Handle Kelvin directly, though usually input is F/C
        if unit_str == 'K':
            final_temp = temp_value + offset
            
        elif default_unit == 'F' or unit_str == 'F':
            conversion_factor = (temp_value - 32) * 5.0 / 9.0
            # If input was just a number, assume C -> add offset directly
            if len(parts) == 1: 
                final_temp = temp_value + offset
            else:
                final_temp = conversion_factor + offset
                
        elif default_unit == 'C' or unit_str in ('C', 'CELSIUS'):
            # If input was just a number, assume C -> add offset directly
            if len(parts) == 1: 
                final_temp = temp_value + offset
            else:
                conversion_factor = (temp_value - 32) * 5.0 / 9.0 # F to C logic used as denominator base? No.
                
        # Let's simplify the logic based on standard inputs usually being numeric or "val unit"

    except ValueError:
        return None
    
    return final_temp

def main():
    """Reads lines from stdin, processes them, and prints Kelvin temperature."""
    
    for line in sys.stdin:
        temp = parse_and_convert(line)
        
        if temp is not None:
            print(f"{temp:.2f}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access required.
    lines_to_process = [
        "75",
        "-40",
        "32 F",
        "100 C",
        "86 F"
    ]
    
    for line in lines_to_process:
        print(line)