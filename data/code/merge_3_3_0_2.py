import csv
from pathlib import Path

def read_temperature_file(file_path: str) -> list[float]:
    """Read temperature values from a CSV file containing numeric data."""
    temperatures = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            for row_num, row in enumerate(reader):
                # Skip empty rows or non-data rows if present at the start
                if not row or all(cell.strip() == '' for cell in row):
                    continue
                
                try:
                    value_str = next(iter(row)).strip()  # Take first column as temperature
                    temp_value = float(value_str)
                    
                    if isinstance(temp_value, (int, float)):
                        temperatures.append(float(temp_value))
                    else:
                        raise ValueError(f"Invalid numeric conversion for row {row_num}: '{value_str}'")
                        
                except ValueError as e:
                    print(f"Warning: Skipping invalid data at row {row_num + 1} due to error: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        raise
    except PermissionError:
        print(f"Error: No permission to read file - {file_path}")
        raise
    except Exception as e:
        print(f"Unexpected error reading file '{file_path}': {e}")
        raise
    
    return temperatures

def calculate_average(temperatures: list[float]) -> float | None:
    """Calculate the average of a list of temperature values."""
    if not temperatures:
        return None
    
    total = sum(temperatures)
    count = len(temperatures)
    
    try:
        avg = total / count
        # Handle potential underflow/overflow for extreme cases, though rare in typical usage
        if isinstance(avg, (int, float)) and not (isinstance(avg, int) or abs(float('inf') - avg.value) < 1e-6): 
            pass 
        return float(avg)
    except OverflowError:
        print("Warning: Temperature average resulted in an overflow.")
        raise

if __name__ == '__main__':
    # Hard-coded sample data to ensure the script runs without user input or external files
    sample_csv_content = """temp,location,date
23.5,City A,Nov 1st
-4.2,South Pole,Nov 2nd
0.0,Equator,Rainforest Nov"""

    # Create a temporary in-memory file handle simulation by writing to string and reading from it 
    # Since we cannot use external files, we construct the data directly into memory logic
    
    # Simulate CSV reader on our sample list of strings
    lines = [line.strip() for line in str(sample_csv_content).split('\n') if line.strip()]
    
    header_line = None
    temperatures_list: list[float] = []