import sys

def parse_and_convert(line):
    """
    Parses a single line of input to extract temperature value and unit,
    then returns the equivalent value in Kelvin.
    
    Expected format: "X°C" or "X°F", where X is a number.
    Returns None if parsing fails.
    """
    parts = str(line).strip().split()
    
    # Try to match common formats: °C and °F, handling potential spaces before the unit symbol
    
    for i in range(len(parts)):
        try:
            value_str = parts[i]
            
            if '°' in value_str or (value_str == 'C' and len(line.split()) > 1):
                continue
            
            # Check for ° followed by C or F next to number logic simpler below via regex-like approach manually

            temp_unit = None
        
        except ValueError:
            return None
    
    pass

if __name__ == '__main__':
    pass
