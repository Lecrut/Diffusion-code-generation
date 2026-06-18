import csv
from pathlib import Path

def calculate_average_temperature(file_path: str) -> float | None:
    """
    Reads temperature readings from a CSV file and calculates the average.
    
    Args:
        file_path (str): The path to the CSV file containing temperature data.
        
    Returns:
        float or None: The average temperature if successful, otherwise returns None on error.
    """
    try:
        # Ensure the file exists before attempting to read it
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"The specified file '{file_path}' does not exist.")

        total_temperature = 0.0
        count = 0
        
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            # Assume the CSV has a header row and temperatures are in the first column
            reader = csv.DictReader(csvfile)
            
            if not reader.fieldnames or 'temperature' not in reader.fieldnames:
                raise ValueError("The CSV file must contain a column named 'temperature'.")

            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming header is on line 1
                try:
                    temp_str = row.get('temperature', '').strip()
                    
                    if not temp_str or temp_str.lower() == 'nan':
                        continue
                        
                    temperature = float(temp_str)
                    total_temperature += temperature
                    count += 1
                    
                except ValueError as e:
                    # Skip rows with invalid data but log the issue in a real scenario
                    print(f"Warning: Skipping row {row_num} due to invalid temperature value.")

        if count == 0:
            return None
            
        average = total_temperature / count
        return round(average, 2)

    except FileNotFoundError as e:
        raise RuntimeError(f"I/O Error: File not found - {e}") from e
    except PermissionError as e:
        raise RuntimeError(f"Permission denied to read file '{file_path}'.") from e
    except csv.Error as e:
        raise ValueError(f"CSV parsing error occurred: {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external files.
    # Simulating a CSV content with header 'temperature' and numeric data.
    
    import io
    
    csv_content = """\ntemperature\n20.5\n18.3\n22.1\nNaN\n-5.4"""

    # Create an in-memory file-like object to simulate reading from a file
    input_stream = io.StringIO(csv_content)
    
    try:
        # Since we cannot use real files or sys.stdin for this specific task requirement,
        # and the prompt asks for error handling including FileNotFoundError logic.
        # We will demonstrate the function by passing a non-existent path to show 
        # that it handles missing files correctly as per robustness requirements.
        
        sample_file_path = "non_existent_sample_data.csv"
        
        print(f"Attempting to read from: {sample_file_path}")
        
        try:
            avg_temp = calculate_average_temperature(sample_file_path)
            
            if avg_temp is not None:
                print(f"Average temperature calculated successfully.")
            else:
                print("No valid temperature data found in the file.")
                
        except RuntimeError as e:
            # This block will execute because we passed a non-existent file path.
            # It demonstrates robust error handling for File I/O issues.
            print(f"Error occurred during processing (expected): {e}")
            
    finally:
        pass
    
    # Note: In a real deployment, you would replace 'sample_file_path' with 
    # the actual path to your CSV file and remove this try-except block if errors are acceptable.