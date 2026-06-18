import sys

def parse_and_convert(line):
    """
    Parses a line containing temperature value and unit (C/F) and converts to Kelvin.
    
    Expected input format: "value C" or "value F" separated by space.
    Returns the converted temperature in Kelvin as an integer, or None if parsing fails.
    """
    parts = line.strip().split()
    try:
        temp_value = float(parts[0])
        unit = parts[1].upper()
        
        if unit == 'C':
            # Convert Celsius to Kelvin: K = C + 273.15, rounded to nearest integer
            kelvin_temp = round(temp_value + 273.15)
        elif unit == 'F':
            # Convert Fahrenheit to Kelvin: K = (F - 32) * 9/5 + 273.15, rounded to nearest integer
            kelvin_temp = round((temp_value - 32) * 9 / 5 + 273.15)
        else:
            return None
            
        return int(kelvin_temp) if isinstance(temp_value, (int, float)) else temp_value
        
    except ValueError:
        return None

def main():
    """
    Reads temperature data from standard input and prints converted Kelvin values to stdout.
    
    Since interactive prompts are forbidden, this function reads lines until EOF.
    However, the task requires a runnable module with hard-coded sample values that run without user input.
    Therefore, we will simulate reading by processing predefined inputs within the main block logic 
    but structured so it can also read from stdin if provided in an environment where allowed (though disallowed per constraints).
    
    To strictly adhere to "never call input(), sys.stdin... or any interactive prompt" while still providing runnable sample data:
    We will use a list of hardcoded strings and iterate over them. This satisfies the requirement 
    that it runs without user input, command-line arguments, network access, or pre-existing files.
    
    If stdin is actually available (which would violate the "no sys.stdin" rule if accessed directly), we prioritize the hard-coded data to ensure no external dependencies are triggered in a typical local run.
    
    Actually, re-reading constraints: "Never call input(), sys.stdin...". 
    So I cannot read from stdin at all. The sample block must be self-contained using hardcoded values only.
    """
    
    # Hard-coded sample data as per requirement to avoid any external dependencies or prompts
    sample_data = [
        "-10 C",
        "25 F",
        "37.5 C",
        "98.6 F"
    ]
    
    for line in sample_data:
        result = parse_and_convert(line)
        if result is not None:
            print(result)

if __name__ == '__main__':
    main()