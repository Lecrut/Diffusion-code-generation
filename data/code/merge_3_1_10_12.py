import csv
from statistics import mean as calculate_mean

def parse_weight_from_csv(file_path):
    """
    Reads weight measurements from a CSV file, converts values to floats,
    and returns the list of weights along with any errors encountered.
    
    Args:
        file_path (str): Path to the CSV file containing numeric data in the first column.
        
    Returns:
        tuple: A tuple containing (weights_list, error_messages).
              weights_list is a list of float values parsed successfully.
              error_messages is a list of strings describing any parsing errors.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If no numeric data could be found in the CSV.
    """
    weights = []
    errors = []

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Iterate through rows to find numeric values (assuming first column is weight)
            for row_num, row in enumerate(reader, start=1):
                if not row or all(cell.strip() == '' for cell in row):
                    continue
                
                try:
                    value = float(row[0].strip())
                    weights.append(value)
                except ValueError as e:
                    errors.append(f"Row {row_num}: Non-numeric entry '{row[0]}'")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    if len(weights) == 0:
        raise ValueError("No valid numeric weight data could be parsed from the CSV.")

    return weights, errors

def calculate_average_weight(file_path):
    """
    Wrapper function to read weights and calculate their average.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        float: The average weight of all valid entries in the file.
    
    Raises:
        FileNotFoundError | ValueError: If parsing fails or no data is found.
    """
    weights, errors = parse_weight_from_csv(file_path)

    if not weights:
        raise ValueError("No valid numeric weight data could be parsed from the CSV.")

    average = calculate_mean(weights)
    
    # Log any non-critical parsing warnings to stderr for debugging without stopping execution
    print(f"Warning - {len(errors)} error(s) encountered during parsing:\n")
    if errors:
        for err in errors:
            print(err, file=__import__('sys').stderr)

    return average

if __name__ == '__main__':
    # Hard-coded sample values simulating a CSV content where the first column contains weights.
    # Format mimics standard CSV structure with headers or data rows.
    
    csv_content = """weight,other_data
70.5,john_doe
68.2,jane_smith
invalid_entry,bob_jones
71.9,charlie_brown
"""

    sample_file_path = "sample_weights.csv"

    # Write the hard-coded content to a temporary file for processing within this script execution context
    with open(sample_file_path, 'w', encoding='utf-8') as f:
        f.write(csv_content)

    try:
        avg_weight = calculate_average_weight(sample_file_path)
        
        print(f"Average weight calculated successfully.")
        print(f"The average weight is {avg_weight:.2f} kg")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=__import__('sys').stderr)
    except ValueError as e:
        print(f"Error: Invalid data encountered - {e}", file=__import__('sys').stderr)