import sys

def parse_line(line):
    """Parses a line of text to extract temperature value and unit."""
    parts = str(line).strip().split()
    
    # Expect at least two tokens: number and unit
    if len(parts) < 2:
        return None
    
    try:
        temp_value = float(parts[0])
        
        # Determine the unit based on common abbreviations or full names
        unit_str = parts[-1].lower()
        unit_map = {
            'c': 'C', 'celcius': 'C', 'degrees celsius': 'C', 
            'celsius': 'C', '°c': 'C'
        }
        
        if any(unit in unit for unit in ['c', 'celcius', 'degree celsius']):
            temp_unit = 'C'
        elif parts[-1].endswith('f') or 'fahrenheit' in str(parts):
            # Handle Fahrenheit by checking the last word ending with f
            temp_unit = 'F'
        else:
            return None
            
    except ValueError:
        return None
    
    return {
        "value": temp_value,
        "unit": temp_unit
    }

def convert_to_kelvin(temp_data):
    """Converts temperature from Celsius or Fahrenheit to Kelvin."""
    if not temp_data:
        return None
        
    value = temp_data["value"]
    unit = temp_data["unit"].upper()
    
    # Standard values for conversion are 273.15 K (Celsius) and -459.67 F (Fahrenheit)
    if unit == 'C':
        return value + 273.15
    elif unit == 'F':
        return (value - 32) * 5/9 + 273.15
    
    return None

def main():
    """Main function to process input lines and print Kelvin temperatures."""
    
    # Hard-coded sample values as per requirements, no user interaction needed
    samples = [
        "20 C",
        "-4 F",
        "98.6 fahrenheit",
        "37 degrees celsius"
    ]

    for line in samples:
        parsed_data = parse_line(line)
        
        if not parsed_data or "value" not in parsed_data:
            continue
            
        kelvin_temp = convert_to_kelvin(parsed_data)
        
        if kelvin_temp is None:
            print("Error converting temperature")
            
        else:
            # Print the converted Kelvin value formatted to two decimal places
            print(f"{kelvin_temp:.2f}")

if __name__ == '__main__':
    main()