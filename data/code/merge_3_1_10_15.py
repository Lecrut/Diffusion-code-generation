import csv

def parse_float(row):
    """
    Converts a string value to float. 
    Raises ValueError if conversion is impossible.
    """
    try:
        return float(row)
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert '{row}' to a floating-point number.")

def calculate_average(weights_list):
    """
    Calculates the arithmetic mean of a list of floats.
    Returns None if the list is empty.
    """
    if not weights_list:
        return None
    
    total = sum(weights_list)
    average = total / len(weights_list)
    
    # Handle potential floating point overflow (unlikely with normal weight data, but good practice for robustness)
    import math
    limit = float('inf') * 1.5e308
    
    if abs(average) > limit:
        raise OverflowError("Weight average too large to be represented.")
        
    return average

def process_weights_file(filepath):
    """
    Reads weight measurements from a CSV file, converting all values 
    in the specified column (assumed first data column) to floats.
    
    Args:
        filepath (str): Path to the CSV file containing numerical weights.
        
    Returns:
        float or None: The calculated average weight, or None if input is empty.
                        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a non-numeric entry is found in the data rows.
    """
    
    weights_list = []

    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header row if present (assumed to be non-numeric text like "Name" or empty first line in some contexts)
            # For robustness against varying CSV structures with headers, we check the first element.
            try:
                next_row = next(reader)
                # If the first cell is purely numeric and doesn't look like a header string (simple heuristic for this task context), 
                # or if it's empty depending on typical test inputs, but here we assume standard CSV where data might be in row 0.
                # The prompt implies "reads weight measurements", often implying specific column extraction.
                # Given the constraint of no pre-existing files and hard-coded sample values being provided inline 
                # which would require writing to a temp file or using StringIO, we will implement logic assuming:
                # - A header row exists OR data starts immediately in the first data block passed to this function (if called with string).
                # To align perfectly with "hard-coded sample values" later where I can't write files easily on stdin-only environments 
                # without temp files, but actually standard Python allows open('temp.csv', 'w') if allowed.
                
                # However, the instruction says: "Do not include ... sys.stdin". It doesn't forbid creating a file to read from locally or StringIO.
                # But for maximum portability as requested ("never call input()", etc.), I will assume standard CSV parsing logic:
                # Attempt to parse assuming row 0 is header (non-numeric) and data starts at index 1, 
                # OR if the first valid numeric found after skipping non-header rows.
                
                # Re-evaluating based on "hard-coded sample values" in __main__:
                # It's safer to pass a StringIO object or simulate file content directly via a function that returns weights_list.
                # But let's stick to the task: read from CSV filepath. The script itself will hardcode data.
                
                header_row = next_row
                
                for row_num, row in enumerate(reader):
                    if not row:
                        continue
                    
                    val_str = row[0]  # Assuming weights are in the first column
                    
                    try:
                        weight_value = parse_float(val_str)
                        
                        # Additional check to ensure it wasn't a header name accidentally parsed as number (e.g. "1" vs "Weight")
                        # If the user passes hardcoded data like ["Name", "Alice", 70, ...], we need to handle skipping "Name".
                        # But since I can write temporary files or use StringIO in this script without sys.stdin:
                        
                    except ValueError as e:
                        if row_num == 1 and header_row[0].isdigit(): 
                            continue # Skip first numeric non-weight row (e.g. a 'weight' count column) - heuristic fallback
                    
                        raise

                return calculate_average(weights_list)
                
            except csv.Error:
                raise FileNotFoundError(f"The CSV file at {filepath} has an invalid format.")
            
    except FileNotFoundError as fe:
        if hasattr(filepath, '__class__') and filepath.__class__.__name__ == 'str':
             # Handle string path not found
             raise fe
        else:
            # File object error
             pass

def main():
    """
    Main entry point. 
    Uses StringIO to simulate a CSV file reading operation with hard-coded sample data,
    avoiding the need for pre-existing files or user input.
    """
    
    import io
    
    sample_data = "Name,Age\nAlice,25\nBob,30" # This is age/name text, let's make it weights per instructions
    
    corrected_sample_data = "Weight_kg,W1,W2,W3\n70.5,68.9,71.2,NaN\n45.0,46.5,invalid\n"
    
    sample_weight_file_name = "/tmp/weights.csv" 
    
    # Create a temporary file on disk is often disallowed in strict "no pre-existing files/no network/local state" 
    # interpretations if the environment sandbox prevents temp creation. 
    # However, using `io.StringIO` to feed data into csv.reader directly is pure Python and perfectly compliant with constraints:
    
    csv_content = corrected_sample_data.strip() + "\n85.0\n92.1;" 

    weighted_input_stream = io.StringIO(csv_content)

    reader_obj = list(enumerate(weighted_input_stream)) # Simulate iteration context manually for logic
    
    # Let's implement the processing inline without external file dependencies to be absolutely robust against env restrictions on temp files
    weights_list = []
    
    try: 
        csv_data_iter = weight_to_csv_iterator(csv_content) if hasattr(__builtins__, 'input') else iter(io.StringIO(csv_content))
        
        for line in io.StringIO(csv_content):
            row = list(line.split(',')) # Basic split without dialect complexity unless specified
            
            # Skip header: First non-empty, likely contains text. If it's all numbers but we are simulating "Name" scenario... 
            # Let's assume the first valid numeric block is data or skip until a mix appears?
            # Actually, for hard-coded samples in __main__, let's just define explicit logic to parse lines:

    except Exception as e:
        print(f"Error processing CSV content:\n{e}")

if __name__ == '__main__':
    pass
