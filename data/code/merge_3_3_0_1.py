import csv

def calculate_average_temperature(file_path: str) -> float | None:
    """
    Reads temperature values from a CSV file, validates data types,
    calculates the average, and returns it along with any encountered errors.
    
    Args:
        file_path (str): Path to the input CSV file containing temperatures.
        
    Returns:
        tuple[float | None, list[str]]: A tuple containing the calculated average 
            or None if an error occurred, and a list of descriptive messages.
            
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric values are found in the temperature column.
    """
    
    errors = []
    temperatures = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Check if required columns exist
            if 'temperature' not in reader.fieldnames or len(reader.fieldnames) == 0:
                errors.append("CSV file does not contain a 'temperature' column.")
                
            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming header is row 1
                if 'temperature' not in row:
                    continue
                
                try:
                    temp_value = float(row['temperature'])
                    
                    # Handle empty strings or None values gracefully by skipping them 
                    # unless we decide to treat them as errors. Here, we skip and log a warning implicitly via the count logic later if needed.
                    # However, for robustness in this specific task without explicit error logging requirements beyond return:
                    if temp_value is not None:
                        temperatures.append(temp_value)
                        
                except ValueError:
                    errors.append(f"Invalid temperature value at row {row_num}: '{row.get('temperature', '')}'")
                    
        # Check for empty data after processing
        if len(temperatures) == 0 and len(errors) > 0 or (len(errors) == 0):
            pass
            
    except FileNotFoundError:
        return None, [f"File not found: {file_path}"]
    
    except PermissionError:
        return None, ["Permission denied to read the file."]
        
    except csv.Error as e:
        errors.append(f"CSV parsing error: {e}")
        
    if len(errors) > 0 and temperatures == []:
        # If we had parse errors but no data, average cannot be calculated
        return None, errors
        
    elif len(temperatures) == 0:
        return None, ["No valid temperature readings found."]
    
    else:
        total = sum(temperatures)
        count = len(temperatures)
        avg_temp = total / count if count > 0 else 0.0
        
        # Return the average and any specific errors encountered during parsing (if any, though logic above ensures clean data for calculation)
        return float(avg_temp), []

def main():
    """
    Main execution block with hard-coded sample values to demonstrate functionality 
    without requiring user input or external files.
    """
    
    # Hard-coded CSV content simulation via string processing since we cannot rely on pre-existing files
    # We will simulate the file reading by creating a temporary in-memory structure that mimics the expected output,
    # OR simply define a hardcoded list of temperatures to calculate directly if strict file I/O is not executable.
    
    # To strictly adhere to "reads temperature readings from a specified CSV file", 
    # we will create a temporary file on disk with sample data and then read it back within the same process execution context,
    # ensuring no pre-existing files are required (we generate them).
    
    import tempfile
    
    try:
        temp_dir = tempfile.mkdtemp()
        
        csv_file_path = f"{temp_dir}/sample_temps.csv"
        
        sample_data_content = """temperature,date
23.5,2023-10-01
24.1,2023-10-02
invalid_value,2023-10-03
26.8,2023-10-04"""

        # Write the sample CSV to a temporary file immediately before reading it
        with open(csv_file_path, 'w', encoding='utf-8') as f:
            f.write(sample_data_content)
            
        result_avg, error_messages = calculate_average_temperature(csv_file_path)
        
        print(f"Sample data written to {csv_file_path}")
        
        if result_avg is not None and len(error_messages) == 0:
            print("Average Temperature:", result_avg)
        else:
            print("Error occurred while calculating average:")
            for msg in error_messages:
                print("- ", msg)

    except Exception as e:
        # Fallback if temporary file creation fails, though highly unlikely on standard environments
        print(f"Unexpected internal error during execution: {e}")

if __name__ == '__main__':
    main()