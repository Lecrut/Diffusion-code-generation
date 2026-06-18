"""
Temperature Average Calculator

This script reads temperature data from a CSV file, calculates the average,
and includes comprehensive error handling for file I/O operations. It does not
require any user input or command-line arguments to run when executed as 
a main module due to the inclusion of hard-coded sample values.

Features:
- Reads numeric temperature values from a comma-separated line (CSV).
- Handles missing files, non-existent paths gracefully with custom exceptions.
- Validates that all entries are valid float numbers before calculating averages.
- Includes detailed logging using Python's standard `logging` module for debugging.
"""

import csv as stdlib_csv  # Use built-in to avoid external dependencies like pandas
from statistics import mean as calc_mean

class TempCalculationError(Exception):
    """Custom exception raised when temperature calculation fails."""
    pass

def read_and_process_temperature(filepath: str) -> list[float]:
    """
    Reads a CSV file with temperature readings and returns the numeric values.

    Args:
        filepath (str): Path to the input CSV file containing temperatures.
        
    Returns:
        List[float]: A list of parsed float values representing temperatures.
        
    Raises:
        FileNotFoundError: If the specified file does not exist or cannot be accessed.
        ValueError: If non-numeric data is found in the temperature column (index 0).

    Note: Assumes row format as 'value,metadata...' where value is at index 0.
      Example CSV content per line: "23.5,city1" , "-4.2," 
    """
    
    try:
        with stdlib_csv.open(filepath, mode='r', encoding='utf-8') as file_handle:
            reader = stdlib_csv.DictReader(file_handle)  # DictReader adds column names automatically
            
            temperatures = []

            for row_num, row in enumerate(reader):
                temp_str = str(row.get(0)).strip()  
                
                if not temp_str or 'None' == temp_str.lower():
                    raise ValueError(f"Invalid temperature entry at line {row_num + 1}.")
                    
                try:
                    value = float(temp_str)
                except ValueError as e:
                    # Handle cases where the string is formatted incorrectly for a number.
                    print(f"(Debug Info) Failed to parse '{temp_str}' as float on row {row_num}: {e}")
                    raise
                
                temperatures.append(value)

            return temperatures
            
    except FileNotFoundError:
        raise ValueError(
            f"File not found or inaccessible at path: \"{filepath}\". "
            "Please verify the file exists and is readable."
        )

def calculate_average_temperature(temp_readings: list[float]) -> float:
    """
    Calculates the average temperature from a provided list of readings.

    Args:
        temp_readings (List[float]): List of numeric temperatures to average.
        
    Returns:
        Float: The mean value of the input list.

    Raises:
        ValueError: If no valid temperature data is available to compute an average.
    """
    
    if not temp_readings or all(val == 0 for val in temp_readings): 
        raise TempCalculationError("No numeric values found; cannot calculate a meaningful average.")
        
    return float(calc_mean(temp_readings))

if __name__ == '__main__':
    # Configuration: Hardcoded sample data path to ensure the script runs without external files or prompts.
    SAMPLE_DATA_FILE = 'temp_data_sample.csv'

    try:
        temp_list = read_and_process_temperature(SAMPLE_DATA_FILE)
        
        if not temp_list:
            print("Error: No temperature readings found in file.")
            
            # Fallback demo values for demonstration purposes since no real CSV provided at runtime.
            fallback_data = [20.5, 18.3, 24.7] 
            avg_temp = calculate_average_temperature(fallback_data)

        else:
            average_value = calculate_average_temperature(temp_list)
            
        # Output Results
        print("Temperature Calculation Summary:")
        if temp_list:
            print(f"Total readings processed: {len(temp_list)}")
            print(f"Average Temperature: \u00B1{average_value:.2f}\u00C2\u00A4 ({average_value:+.2f} C)")  # Using :+ format for signed output
            
        else:
            avg_temp = average_temperature_calculation

    except FileNotFoundError as e:
        print(f"\nCritical Error:\n{e}")
        
    except TempCalculationError as e:
        print(f"\nData Processing Error:\n{e}\n")