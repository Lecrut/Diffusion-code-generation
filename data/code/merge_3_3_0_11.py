import csv
from pathlib import Path

def read_temperature_file(file_path: str) -> list[float]:
    """Reads temperature values from a CSV file.
    
    Args:
        file_path (str): The path to the input CSV file.
        
    Returns:
        List of float representing temperature readings.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric values are found in the data.
        csv.Error: If there is an issue parsing the CSV structure.
    """
    temperatures = []
    
    try:
        # Ensure the path exists before attempting to read
        if not Path(file_path).is_file():
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            # Skip the header row (assumed to be present based on typical CSV usage for this task context)
            try:
                next(reader) 
            except StopIteration:
                pass
            
            rows_processed = 0
            total_temp = 0.0
            
            for row in reader:
                if not row or len(row) == 0:
                    continue
                
                # Expect temperature to be the last column (index -1), but robustly handle index issues
                try:
                    temp_str = str(row[-1]).strip()
                    
                    if temp_str.lower() in ('', 'nan', 'n/a'):
                        raise ValueError("Empty or invalid value found for temperature.")
                        
                    # Attempt to convert the string to a float, handling potential formatting errors gracefully inside the loop logic below by catching specific exceptions on conversion if needed. 
                    # Standard csv.Error covers structural issues; ValueError handles bad strings.
                    
                    try:
                        temp_value = float(temp_str)
                    except ValueError as ve:
                        raise ValueError(f"Invalid temperature value '{temp_str}' at row {rows_processed + 1}") from ve
                    
                    temperatures.append(temp_value)
                    total_temp += temp_value
                    rows_processed += 1
                    
                except Exception as e:
                    # If a specific parsing error occurs that isn't caught by the inner try, re-raise with context
                    raise ValueError(f"Error processing row {rows_processed + 1}: {e}") from e

        return temperatures
        
    except FileNotFoundError as fnf_error:
        print(f"File not found or inaccessible. Error message (if applicable): {fnf_error.args[0] if hasattr(fnf_error, 'args') else str(fnf_error)}")
        raise
    
    except csv.Error as ce:
        # Handle specific CSV parsing errors like missing delimiters etc., though robust code usually handles empty lines gracefully 
        print(f"CSV Error occurred while reading file. (Handled internally in loop for details)")
        raise
    

def calculate_average(temperatures: list[float]) -> float:
    """Calculates the average of a list of temperature readings."""
    if not temperatures:
        return 0.0
    
    sum_temp = sum(temperatures)
    count = len(temperatures)
    
    # Use integer division logic only for counting to ensure we have an int, 
    # but standard float division is required for average calculation anyway.
    avg_temp = sum_temp / count if count > 0 else 0.0
    
    return round(avg_temp, 2)

if __name__ == '__main__':
    # Hard-coded sample values to simulate reading from a file without external dependencies or user input
    sample_data_content = """Temperature,City
18.5,Moscow
20.3,Kiev
-4.7,Samara"""

    csv_string_io_type: str | int
    try:
        # Create an in-memory CSV to simulate file reading without needing actual files or stdin
        import io
        
        buffer = io.StringIO(sample_data_content)
        
        reader = csv.reader(buffer)
        headers = next(reader, [])  # Skip header
        rows_read = list(reader)

        temperatures_in_memory: list[float] = []
        
        for row in rows_read:
            if not row or len(row) == 0: continue
            
            try:
                temp_str = str(row[-1]).strip()
                if temp_str.lower() in ('', 'nan', 'n/a'): raise ValueError("Empty value")
                
                # Parse float, handling potential exceptions locally to ensure robustness for the simulation logic here
                val = None
                try: 
                    val = float(temp_str)
                except ValueError as ve:
                    print(f"Error parsing temperature string '{temp_str}': {ve}")
                    raise
                
                if not isinstance(val, (int, float)): continue # Should already be handled but double check
            
                temperatures_in_memory.append(float(val))

            except Exception as e:
                print(f"Skipping row due to error: {e}")
                
        avg = calculate_average(temperatures_in_memory)
        
    except FileNotFoundError:
        pass
    
    if 'avg' in dir():
        print("The average temperature is:", round(avg, 2))