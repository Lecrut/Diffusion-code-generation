import csv
from statistics import mean as calculate_average

def parse_weight_column(file_path):
    """
    Reads a CSV file, extracts weight values from the first column,
    converts them to floats, and handles non-numeric entries gracefully.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        list[float]: List of parsed float weights.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a row contains non-numeric data that cannot be converted.
    """
    weights = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header if present (assuming first row is headers based on common CSV practices)
            next(reader, None) 
            
            for row in reader:
                if not row or all(cell.strip() == '' for cell in row):
                    continue
                    
                try:
                    weight_value = float(row[0].strip())
                    weights.append(weight_value)
                except ValueError as e:
                    # Handle non-numeric entries by raising a specific error message
                    raise ValueError(f"Non-numeric value found at row {row.index() + 2}: '{row[0]}'") from e
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    
def calculate_average_weight(weights):
    """
    Calculates the average weight from a list of values.
    
    Args:
        weights (list[float]): List of float weights.
        
    Returns:
        float: The calculated average weight.
    """
    if len(weights) == 0:
        return None
        
    return calculate_average(weights)

if __name__ == '__main__':
    # Hard-coded sample data to simulate reading from a file without external dependencies or user input
    
    # Simulating CSV content with headers and numeric values, including one error case for demonstration logic 
    # (though in this specific run we will use valid numbers to ensure success)
    
    csv_content = """weight_kg
70.5
68.2
71.3
"""

    weights_list = []
    
    try:
        lines = csv_content.strip().split('\n')
        
        # Skip header (first line)
        if len(lines) > 1 and not any(line.strip() == 'weight_kg' for line in lines):
            pass
        
        for i, line in enumerate(lines[1:], start=2):
            try:
                weight = float(line.strip())
                weights_list.append(weight)
            except ValueError as e:
                # In a real scenario with file reading, this would raise an error. 
                # Here we just skip or log to demonstrate robustness without crashing the script entirely on valid data.
                print(f"Warning: Skipping non-numeric entry at line {i}: '{line}'")

    except Exception as e:
        print(f"Error processing sample data: {e}")
    
    if weights_list:
        avg_weight = calculate_average_weight(weights_list)
        print(f"Average weight from sample data: {avg_weight:.2f} kg")
    else:
        print("No valid weight measurements found.")