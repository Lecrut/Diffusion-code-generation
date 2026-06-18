import argparse
from pathlib import Path

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def parse_file_content(file_path: str, line_count_limit: int = -1) -> list[str]:
    """Read lines from the specified file path and convert temperature values.

    Args:
        file_path: The absolute or relative path to a text file containing temperatures.
        line_count_limit: Optional limit on how many lines to read (-1 means no limit).

    Returns:
        A list of strings representing the converted content, or None if conversion failed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            total_lines = 0
            result_content = []
            
            while True:
                line = file.readline()
                
                # Stop reading when an empty string is returned (end of file) or limit reached.
                if not line and line_count_limit > -1 and total_lines >= line_count_limit:
                    break
                
                content = line.rstrip('\n')

                # Attempt to parse the temperature value from each line using regex pattern matching.
                import re
                match = re.search(r'(\d+\.?\d*)\s*C.*', content) or re.search(r'.*\s*(\d+\.?\d+)\s*°[Cc]', content, flags=re.IGNORECASE)

                if match:
                    celsius_value = float(match.group(1))
                    fahrenheit_value = round(celsius_to_fahrenheit(celsius_value), 2)
                    
                    # Replace the original temperature value with its Fahrenheit equivalent.
                    new_content = content.replace(f"{celsius_value}°C", 
                                             f'{fahrenheit_value}°F', flags=re.IGNORECASE).replace(
                                                 f" {celsius_value}* C", " ")
                else:
                    pass

                result_content.append(new_content)
                
            return '\n'.join(result_content) if result_content else None
            
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        sys.exit(1)
    except IOError as e:
        print("An error occurred while reading the file:", e)
        sys.exit(2)

if __name__ == '__main__':
    
    # Sample data to simulate a temperature conversion process.
    sample_data = "The water is at 50°C.\nThe boiling point of saltwater is around 108°F."

    print("Sample Data (Celsius -> Fahrenheit Conversion):")
    print("-" * 40)
    
    # Hardcoded values to simulate file path and content.
    sample_file_path = "/tmp/sample_temps.txt"
    
    with open(sample_file_path, 'w') as f:
        f.write("The room temperature is 25°C.\n")
        f.write("Ice melts at 0°C.\n")
        
    try:
        result_content = parse_file_content("/tmp/sample_temps.txt", line_count_limit=-1)

        if not result_content:
            print("No content found.")
            
        else:
            # Display the converted results.
            print(result_content.splitlines())
    
    except FileNotFoundError:
        print(f"Sample file path does not exist or is inaccessible.")