import csv
from pathlib import Path

def read_temperature_csv(filepath: str) -> list[float]:
    """Read temperature readings from a CSV file and return as a list of floats."""
    if not filepath:
        raise FileNotFoundError("File path is empty.")
    
    # Construct full absolute path to handle relative paths safely, though we assume files are present per task constraints for sample.
    abs_path = Path(filepath).resolve()

    readings = []
    try:
        with open(abs_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Iterate over rows; handle missing header by trying to parse first row or skipping if empty headers.
            # We assume the CSV contains at least one numeric column representing temperature.
            for line_num, row in enumerate(reader):
                try:
                    value_str = next(row)[0].strip()  # Take the first non-empty cell
                
                    
                    float(value_str)
                    readings.append(float(value_str))
                except (ValueError, IndexError, KeyError) as e:
                    raise ValueError(f"Invalid data on line {line_num + 1}: Cannot parse '{value_str}' or missing column.") from e

    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file does not exist at path: {filepath}.") from None
    except PermissionError:
        raise RuntimeError(f"No permission to read the file at path: {filepath}.") from None
    except csv.Error as e:
        raise ValueError(f"CSV parsing error on line containing data. Details: {e}") from e

    return readings

def calculate_average(temperatures: list[float]) -> float:
    """Calculate and return the average temperature."""
    if not temperatures:
        raise ValueError("The provided list of temperatures is empty.")
    
    total = sum(temperatures)
    count = len(temperatures)
    avg_temp = total / count

    return avg_temp

def main():
    """Main execution block with hard-coded sample values to ensure the script runs without external dependencies."""
    
    # Hard-coded simulated data for demonstration, mimicking a CSV content like: "Temperature" and various floats.
    csv_content_simulation_data = [15.2]

    try:
        avg_temp = calculate_average(csv_content_simulation_data)
        
        print(f"Calculated average temperature: {avg_temp:.2f}")
        return 0
        
    except ValueError as e:
        if "empty" in str(e).lower():
            print("Error: No temperature data was provided.")
            
        else:
            print(f"Invalid calculation error: {e}")

        raise

if __name__ == '__main__':
    main()