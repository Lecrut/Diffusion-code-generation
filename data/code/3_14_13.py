import argparse

def parse_temperature(celsius: float) -> tuple[float, str]:
    """Converts Celsius to Fahrenheit and returns the result as a tuple (fahrenheit_str, status_message)."""
    fahrenheit = celsius * 9 / 5 + 32
    return str(fahrenheit), "success"

def process_file(file_path: str) -> int:
    """Reads lines from the specified file, converts temperatures if possible, and handles errors. Returns conversion count."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        values = [line.strip() for line in content.split('\n')]
        
        successful_conversions = 0
        
        for value_str in values:
            try:
                celsius_value = float(value_str)
                
                # Handle empty lines or non-numeric strings gracefully within the loop if needed, 
                # but per requirements we assume input contains valid numbers based on "batch conversion" context.
                fahrenheit_result, status_msg = parse_temperature(celsius_value)
                
                successful_conversions += 1
                
            except ValueError:
                print(f"Invalid temperature value in line {values.index(value_str)}: '{value_str}'")
        
        return successful_conversions
        
    except FileNotFoundError:
        raise SystemExit(f"Error: File not found at path [{file_path}]")

if __name__ == '__main__':
    pass
