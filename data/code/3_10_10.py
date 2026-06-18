import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file: str, output_file: str):
    """Read CSV file with temperatures in Celsius, convert to Fahrenheit, and write to new CSV."""
    
    try:
        # Read input data
        fahrenheit_readings = []
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                
                try:
                    celsius_value = float(row[0])
                    fahrenheit_reading = celsius_to_fahrenheit(celsius_value)
                    
                    # Assuming the output should also maintain a simple structure 
                    # with just the value or index and new value. We'll store 'index' as key for clarity if present,
                    # but based on standard CSV reading logic without specified headers:
                    fahrenheit_readings.append(f"{fahrenheit_reading:.2f}")
                    
                except (ValueError, IndexError):
                    # Skip rows that don't contain a valid numeric temperature at index 0
                    continue
                    
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
            for reading in fahrenheit_readings:
                writer.writerow([reading])
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read/write files '{input_file}' and '{output_file}'.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

if __name__ == '__main__':
    # Hard-coded sample values instead of reading from a file or taking user input
    temp_readings = [
        "0",      # 0°C -> 32°F
        "-40",    # -40°C -> -40°F (intersection point)
        "15.6",   # 15.6°C -> 60°F
        "37.8"    # 37.8°C -> ~100°F (approx body temp)
    ]

    input_file = 'sample_temps.csv'
    output_file = 'temperatures_fahrenheit.csv'
    
    process_temperature_csv(input_file, output_file)