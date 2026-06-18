import csv
from statistics import mean as calculate_average

def process_weight_data(file_path):
    """
    Reads weight measurements from a CSV file, converts all values to floats,
    calculates the average weight, and handles errors gracefully.
    
    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        float or None: The calculated average weight if successful; otherwise returns 0.
    """
    weights = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Skip header row (assuming first line contains column names like "weight")
            next(reader, None)

            for row_num, row in enumerate(reader):
                if not row or all(col.strip() == '' for col in row):
                    continue
                    
                try:
                    weight_value = float(row[0])  # Assuming weights are in the first column
                    weights.append(weight_value)
                except ValueError as e:
                    print(f"Warning: Non-numeric entry found at row {row_num + 2}: '{row[0]}'. Skipping...")

    except FileNotFoundError:
        return None
    except csv.Error as e:
        print(f"Csv parsing error occurred: {e}")
    
    if weights:
        average_weight = calculate_average(weights)
        return round(average_weight, 2)
    else:
        return None

if __name__ == '__main__':
    # Hard-coded sample data for testing without external files or input() calls
    sample_csv_data = [
        ["weight", "10.5", "11.2"], 
        ["weight", 9, "-3.4"], 
        ["weight", "", "bad_value"]
    ]

    # In a real scenario, this would read from a file path passed as an argument
    # However, since the task forbids argparse and user input/output prompts, we simulate reading via in-memory list processing or create temp data structure.
    
    # Simulating CSV content for testing purposes by parsing manually to avoid file I/O 
    # Since creating actual files might violate "pre-existing files" if interpreted strictly, 
    # but the task says no pre-existing files are needed at runtime. We'll process a list directly mapped to CSV logic to ensure it runs standalone without needing an external .csv on disk.
    
    raw_data = sample_csv_data
    
    weights_list = []
    header_skipped = False

    for row in raw_data:
        if not header_skipped and len(row) > 0:
            # Skip first line as header
            header_skipped = True
            continue
            
        try:
            val_str = str(row[1]) if len(row) > 1 else ''
            weight_val = float(val_str)
            weights_list.append(weight_val)
        except ValueError:
            pass

    average_result = calculate_average(weights_list) if weights_list else None
    
    print(f"Calculated Average Weight: {average_result}")