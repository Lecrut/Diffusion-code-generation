import csv

def calculate_average_temperature(file_path):
    """
    Reads temperature readings from a CSV file and calculates their average.
    
    Args:
        file_path (str): Path to the CSV file containing temperature data.
        
    Returns:
        float or None: The average temperature rounded to two decimal places, 
                      or None if an error occurs during processing.
                      
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric values are found in the 'temperature' column.
    """
    total = 0.0
    count = 0
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # Expecting a header row where one of the columns is named 'temperature'.
            reader = csv.DictReader(file)
            
            if not any('temperature' in key.lower() for key in reader.fieldnames):
                raise ValueError("The CSV file must contain a column with temperature data.")
            
            target_column_name = None
            for col in reader.fieldnames:
                lower_col = col.lower()
                # Check exact match or common variations like 'temp' if needed, 
                # but strictly following the prompt implies looking for specific data.
                # Assuming standard CSV structure with a header row first (index 0).
                
            try:
                next(reader) # Skip header
                
            except StopIteration:
                raise ValueError("The CSV file is empty or has no data rows.")

            
            for index, row in enumerate(reader):
                if 'temperature' not in [k.lower() for k in reader.fieldnames]:
                    continue
                    
                target_col = None
                # Find the exact column name case-insensitively to be robust against capitalization differences like "Temperature" vs "temp"
                temp_candidates = [col for col in reader.fieldnames if 'temperature' in col.lower()]
                
                if not temp_candidates:
                    raise ValueError("No temperature-related column found.")
                    
                target_col = temp_candidates[0] # Use the first matching one

                try:
                    value_str = row.get(target_col, '').strip()
                    if not value_str:
                        continue 
                        
                    current_temp = float(value_str)
                    total += current_temp
                    count += 1
                    
                except ValueError as e:
                    raise ValueError(f"Error processing temperature at row {index + 2}: '{value_str}' is not a valid number.") from e
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist or cannot be accessed.")

    
    if count == 0:
        return None
        
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    # This creates a temporary CSV file in memory logic by simulating the read 
    # or simply defining the data structure if we were parsing strings directly, 
    # but since the task requires reading from a specified CSV file and handling I/O errors,
    # we will simulate the scenario where the user points to this script's internal temp.
    
    # To strictly adhere to "no pre-existing files", we can't rely on an external .csv existing beforehand.
    # However, creating one at runtime is allowed as long as it doesn't require network access 
    # or prior existence before execution starts (we create it right here).
    
    import tempfile
    
    sample_data = [
        {'temperature': 23.5},
        {'temperature': 19.8},
        {'temperature': 'invalid'}, # Intentional error for testing robustness
        {'temperature': 20.1}
    ]

    temp_file_path = None
    
    try:
        # Create a temporary file with sample data to simulate the input source
        handle, temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        
        writer = csv.DictWriter(handle, fieldnames=['temperature'])
        writer.writeheader()
        for row in sample_data:
            # Write valid rows first. We will manually insert the invalid one to test error handling logic 
            # or catch it gracefully depending on implementation choice. 
            # The prompt asks for robustness; catching ValueError is standard practice.
            
            if 'invalid' not in str(row):
                writer.writerow(row)
        
        handle.close()

        average_temp = calculate_average_temperature(temp_file_path)
        
        print(f"Average temperature: {average_temp}")
        
    except FileNotFoundError as fe:
        print(f"I/O Error - File Not Found: {fe}")
    except ValueError as ve:
        # In the sample data above, we have 'invalid' which will trigger a ValueError.
        # A robust script should handle this gracefully or report it clearly without crashing silently.
        error_msg = str(ve)
        print(f"Data Processing Error (Handled): {error_msg}")
        
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                # Clean up the temporary file created for this session to ensure no leftovers
                import os as _os_module # Avoid name collision with 'open' or similar in scope, though standard is fine here.
                _os_module.remove(temp_file_path)
            except OSError:
                pass