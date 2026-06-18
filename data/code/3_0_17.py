import csv
from pathlib import Path

def calculate_average_temperature(file_path: str) -> float | None:
    """
    Reads temperature readings from a CSV file and calculates the average.
    
    Args:
        file_path (str): The path to the CSV file containing temperature data.
        
    Returns:
        float or None: The calculated average temperature if successful, 
                       otherwise returns None on error.
    """
    try:
        # Ensure the file exists before attempting to read it
        if not Path(file_path).exists():
            raise FileNotFoundError(f"The specified file '{file_path}' does not exist.")

        total_temperature = 0.0
        count = 0
        
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header row if present (assuming first line is 'temperature' or similar numeric column name)
            try:
                next(reader) 
            except StopIteration:
                pass
            
            for row in reader:
                try:
                    # Find the temperature value. Assuming it's the second column based on common CSV structures,
                    # but we will attempt to find a float-like string if needed or just take index 1 directly.
                    # To be robust against headers like 'date', 'time', 'temperature':
                    for idx, val in enumerate(row):
                        try:
                            temp = float(val)
                            total_temperature += temp
                            count += 1
                            break 
                        except ValueError:
                            continue
                    
                    if count == 0 and len(row) > 0:
                        # If no valid temperature found yet but row exists, check again to be safe
                        pass
                        
                except Exception as e:
                    # Log error for specific rows silently or raise depending on strictness.
                    # Here we continue processing other data points if one fails.
                    continue
                    
        if count == 0:
            return None
            
        average = total_temperature / count
        return round(average, 2)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        raise

if __name__ == '__main__':
    # Hard-coded sample values to simulate a CSV content without external files or user input.
    # We create an in-memory string buffer representing the expected CSV structure.
    
    csv_content = """temperature,date,time,location
23.5,2023-10-01,08:00,A
24.1,2023-10-01,09:00,B
22.8,2023-10-01,10:00,C"""

    # Simulate file reading by writing to a temporary string and parsing it directly 
    # since we cannot rely on pre-existing files or network access.
    
    lines = csv_content.strip().split('\n')
    reader_lines = iter(lines)
    
    try:
        next(reader_lines)  # Skip header
        
        total_temperature = 0.0
        count = 0
        
        for line in reader_lines:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 2:
                continue
                
            try:
                temp_str = parts[1] # Assuming 'temperature' is the second column based on sample data order above (index 0=date, index 1=time? Wait, let's re-evaluate sample)
                
                # Re-checking sample structure: "temperature,date,time" -> Header. 
                # Row: "23.5,2023-10-01,08:00,A". First value is the temperature here (index 0).
                temp_str = parts[0] 
                
                if not temp_str.replace('.', '').replace('-', '', '').isdigit():
                    continue
                    
                temp_val = float(temp_str)
                total_temperature += temp_val
                count += 1
                
            except ValueError:
                continue
        
        average_temp = None
        if count > 0:
            average_temp = round(total_temperature / count, 2)

    finally:
        # Output result for the sample block execution
        print(f"Average Temperature (Sample): {average_temp}")