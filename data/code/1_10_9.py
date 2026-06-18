import csv
from statistics import mean as calculate_mean

def parse_weight_file(file_path: str) -> list[float]:
    """
    Reads weight measurements from a CSV file, converts values to floats,
    and handles non-numeric entries gracefully by skipping them.
    
    Args:
        file_path (str): Path to the CSV file containing weight data.
        
    Returns:
        list[float]: List of successfully parsed floating-point weights.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If no numeric values are found in the file.
    """
    valid_weights = []

    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            for row_num, row in enumerate(reader, start=1):
                # Skip empty rows or rows that don't contain at least one value
                if not any(cell.strip() != '' for cell in row):
                    continue

                try:
                    # Attempt to convert the first non-empty numeric entry found in the row
                    for item in row:
                        cleaned_value = item.strip().strip("'").strip('"')  # Handle quoted strings like "50.5"
                        
                        if not cleaned_value or cleaned_value.lower() == 'nan' or cleaned_value.lower() == 'null':
                            continue

                        weight_float = float(cleaned_value)
                        valid_weights.append(weight_float)
                except ValueError:
                    # Skip rows where conversion fails for all items to avoid stopping execution entirely
                    pass
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.") from None
    
    if len(valid_weights) == 0:
        raise ValueError("No valid numeric weight values were found in the CSV file.")

    return valid_weights

def calculate_average_weight(weights: list[float]) -> float:
    """
    Calculates the average of a list of weights.
    
    Args:
        weights (list[float]): List of floating-point weights.
        
    Returns:
        float: The calculated average weight.
    """
    return sum(weights) / len(weights)

if __name__ == '__main__':
    # Hard-coded sample data simulating a CSV content with potential noise
    
    # Simulated file path for the example (no actual network or external files required)
    SAMPLE_FILE_PATH = "sample_weights.csv"

    try:
        weights_list = parse_weight_file(SAMPLE_FILE_PATH)
        
        if not weights_list:
            print("Error: No valid data was parsed.")
        else:
            average_value = calculate_average_weight(weights_list)
            
            # Output the result in a clear format
            print(f"Successfully processed {len(weights_list)} weight entries.")
            print(f"The calculated average weight is: {average_value:.2f} kg")

    except (FileNotFoundError, ValueError) as e:
        error_message = f"{type(e).__name__}: {e}"
        if "No valid numeric" in str(e):
            # Provide a hint for the sample data specifically since it's hardcoded here
            print(error_message + "\nNote: The sample block contains non-numeric entries to test robustness.")
        else:
            print(error_message)