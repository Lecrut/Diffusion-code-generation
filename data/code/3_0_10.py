import csv
from pathlib import Path

def calculate_average_temperature(file_path: str) -> float | None:
    """
    Reads temperature values from a CSV file, validates data types,
    and calculates the average. Returns None if no valid temperatures are found.
    
    Args:
        file_path (str): The path to the input CSV file containing 'temperature' column.
        
    Returns:
        float | None: The calculated average temperature or None on failure/empty data.
    """
    try:
        # Ensure we have a valid Path object for consistent operations
        csv_file = Path(file_path)
        if not csv_file.exists():
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        temperatures = []
        
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Check if the required 'temperature' column exists in the CSV header
            if reader.fieldnames is None or 'temperature' not in reader.fieldnames:
                raise ValueError(f"CSV file missing expected 'temperature' column. Available columns: {reader.fieldnames}")

            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming a header on line 1
                try:
                    temp_str = row['temperature'].strip()
                    
                    if not temp_str or temp_str.lower() == 'nan':
                        continue
                        
                    temperature_value = float(temp_str)
                    temperatures.append(temperature_value)
                    
                except ValueError as ve:
                    # Skip rows with invalid numeric data but do not stop execution entirely
                    print(f"Warning: Skipping row {row_num} due to non-numeric value '{temp_str}'.")

        if len(temperatures) == 0:
            return None
            
        average_temp = sum(temperatures) / len(temperatures)
        
    except FileNotFoundError as fnf_err:
        print(f"Error: {fnf_err}")
        raise
    except PermissionError as pe_err:
        print(f"Permission denied accessing file: {file_path}.")
        raise
    except csv.Error as ce_err:
        print(f"CSV parsing error occurred: {ce_err}")
        raise
        
    return average_temp

if __name__ == '__main__':
    # Hard-coded sample data simulation since no external files are allowed to exist.
    # We will create a temporary file in memory logic by reading from a string buffer 
    # or simply define the calculation directly if we treat the "file" as an internal constant,
    # but strictly following the requirement of reading from a specified CSV implies structure.
    
    # To satisfy "reads temperature readings from a specified CSV file" without pre-existing files:
    # We will simulate the file path pointing to a temporary location that gets populated 
    # or we can define the data directly in a way that mimics the read process for robustness testing.
    # However, the prompt says "Do not include ... pre-existing files". Creating one during runtime is acceptable 
    # as long as it's transient and doesn't rely on user input. 
    
    # Let's create a temporary file with sample data to demonstrate functionality without external dependencies.
    
    import tempfile
    
    temp_data = [32, 45, "nan", None, -10]