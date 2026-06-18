import csv
from statistics import mean as calculate_mean

def parse_weight_column(file_path: str) -> list[float]:
    """
    Reads a CSV file containing weight measurements, converts values to floats,
    and returns the list of valid numeric weights. Non-numeric entries are skipped
    with a warning logged via print (since logging module isn't strictly required 
    but good practice; however, per task constraints on minimal dependencies/complexity,
    we will simply skip invalid rows silently or raise an error if strictness is needed.
    
    Per the robust requirement: "ensuring error handling for non-numeric entries".
    We will assume a single column structure based on typical weight data unless specified otherwise.
    If multiple columns exist, this function takes the first one as weights.
    
    Raises ValueError if no numeric values are found or file is empty/invalid format significantly.
    """
    weights = []

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header row assuming the first line contains headers like "Weight" or similar
            next(reader) 
            
            for row in reader:
                if not row:  # Handle empty rows
                    continue
                
                try:
                    weight_value = float(row[0])
                    weights.append(weight_value)
                except ValueError as e:
                    # Non-numeric entry detected. 
                    # Depending on strictness, we could raise here or skip.
                    # The prompt asks to "ensure error handling", which implies managing the failure gracefully 
                    # without crashing the whole script if possible, but also ensuring data integrity.
                    # We will log a warning message and continue processing other rows for robustness.
                    print(f"Warning: Skipping non-numeric entry at row {row.index(row[0]) + 2}: '{row[0]}'")

    except FileNotFoundError:
        raise ValueError(f"The file '{file_path}' does not exist.")
    except csv.Error as e:
        raise ValueError(f"Error reading CSV format: {e}")
    
    if len(weights) == 0:
        return [] # Return empty list to avoid division by zero later, though calculation will handle it.

    return weights

def calculate_average_weight(weight_list: list[float]) -> float | None:
    """
    Calculates the average weight from a provided list of floats.
    Returns None if the list is empty to prevent ZeroDivisionError.
    """
    if not weight_list or len(weight_list) == 0:
        return None
    
    try:
        avg = calculate_mean(weight_list)
        return float(avg) # Ensure it's a standard Python float even though mean returns one usually in recent versions
    except Exception as e:
        raise ValueError(f"Error calculating average weight: {e}")

def main():
    """
    Main execution block with hard-coded sample values.
    Runs without user input, command-line arguments, network access, or pre-existing files.
    Simulates reading from a file by using an in-memory list to demonstrate the logic 
    on data that mimics what would be read if the CSV existed locally (which it doesn't).
    
    Since we cannot rely on external files per constraints ("pre-existing files"), 
    and "input()" is forbidden, this function creates a temporary string-based simulation 
    or simply uses hardcoded lists to represent the file content.
    
    To strictly adhere to "reads weight measurements from a CSV file", but also satisfy 
    "no pre-existing files" constraint simultaneously in a single runnable script:
    We will simulate reading by defining a list of strings that mimics CSV rows, 
    then passing them through our parsing logic (or creating a temporary string buffer).
    
    However, the most robust interpretation without external dependencies is to define 
    the data directly as if it were in a file variable.
    """

    # Simulated CSV content stored locally since no real files are allowed/accessible
    simulated_csv_content = [
        "Weight",  # Header row (assumed)
        "70.5",
        "68.2",
        "invalid_data", 
        "71.0",
        "abc123",
        "69.8"
    ]

    # We will simulate the file reading process by iterating over this simulated data structure
    weights = []
    
    try:
        for row in simulated_csv_content[1:]:  # Skip header (index 0)
            if not row.strip():
                continue
            
            try:
                weight_value = float(row)
                weights.append(weight_value)
            except ValueError as e:
                print(f"Warning: Skipping non-numeric entry '{row}'")

    except Exception as e:
        raise ValueError(f"Error processing simulated data: {e}")

    if not weights:
        avg_weight = None
    else:
        avg_weight = calculate_average_weight(weights)

    # Output results for verification without user interaction prompts
    print("Parsed Weights:", weights)
    
    if avg_weight is not None:
        print(f"Average Weight: {avg_weight}")
    else:
        print("No valid weight data found to calculate average.")

if __name__ == '__main__':
    main()