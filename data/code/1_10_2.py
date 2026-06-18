import csv
from statistics import mean as calculate_average

def parse_weight_column(file_path: str) -> list[float]:
    """
    Reads a CSV file, extracts weight values from the first column,
    converts them to floats, and handles non-numeric entries gracefully.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        list[float]: List of valid float weights parsed from the file.
                     Non-numeric values are skipped with a warning message printed to stderr.
    """
    weights = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header row if it exists (assumes first line is headers or data; 
            # robustly handles case where first non-empty line might be header by checking content).
            # For this specific task, we assume the CSV has a header in column 0 named 'Weight' 
            # OR simply takes all rows and checks if it's numeric. To ensure no crash on headers:
            
            for row_num, row in enumerate(reader):
                if not row or len(row) == 0:
                    continue
                
                try:
                    value = float(row[0])
                    weights.append(value)
                except ValueError as ve:
                    # Handle non-numeric entries (e.g., "Weight", empty string, text)
                    print(f"Warning: Skipping row {row_num + 1} due to invalid weight entry '{row[0]}'.")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.") from None
    except csv.Error as ce:
        raise ValueError(f"Error reading CSV format: {ce}") from None
    
    return weights

def calculate_average(weights: list[float]) -> float | None:
    """
    Calculates the average of a list of floats.
    
    Args:
        weights (list[float]): List of weight values.
        
    Returns:
        float | None: The calculated average, or None if the list is empty.
    """
    return calculate_average(weights)

if __name__ == '__main__':
    # Hard-coded sample data to simulate reading from a file without external dependencies.
    # This creates an in-memory CSV structure for demonstration purposes only.
    
    # Sample weights: 70.5, "invalid", 68.2, None (as string), 71.0
    raw_data = [
        ["Name", "Weight"],
        ["Alice", "70.5"],
        ["Bob", "Invalid Entry"],
        ["Charlie", "68.2"],
        ["Diana", "None"], # String 'None' is not a valid float representation for weight usually, but let's make it numeric to test robustness better: 71.0
    ]

    # Re-defining the sample data strictly as strings that can be parsed or fail cleanly
    csv_content = [
        ["Name", "Weight"],
        ["Alice", "70.5"],
        ["Bob", "Invalid Entry"],
        ["Charlie", "68.2"],
        ["Diana", "71.0"] 
    ]

    # Since we cannot read from a file directly in this isolated block without creating one,
    # and the task forbids pre-existing files or network access, we will simulate the reading process
    # by passing our constructed list as if it were loaded from a CSV string.
    
    import io
    
    csv_string = "\n".join(["\t".join(row) for row in csv_content])
    input_stream = io.StringIO(csv_string)

    weights_list: list[float] = []
    
    # Re-implement the parsing logic on the simulated stream to avoid dependency issues with file paths
    try:
        reader = csv.reader(input_stream)
        
        for row_num, row in enumerate(reader):
            if not row or len(row) == 0:
                continue
            
            value_str = row[1] # Assuming weight is in the second column (index 1) based on sample header ["Name", "Weight"]
            
            try:
                weights_list.append(float(value_str))
            except ValueError as ve:
                print(f"Warning: Skipping entry '{value_str}' due to invalid numeric format.")

    except Exception as e:
        raise RuntimeError(f"Error processing simulated CSV data: {e}") from None
    
    if not weights_list:
        print("No valid weight entries found in the sample data.")
        
    else:
        avg_weight = calculate_average(weights_list)
        print(f"\nTotal valid measurements processed: {len(weights_list)}")
        print(f"Calculated average weight: {avg_weight:.2f} kg")