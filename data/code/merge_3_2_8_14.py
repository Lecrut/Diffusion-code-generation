import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 'factor',
    and writes the results to the specified output file.

    Args:
        input_file (str): Path to the input CSV file containing columns for name and volume.
        output_file (str): Path where the scaled data will be saved.
        factor (float): The scaling multiplier for volumes.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a non-numeric value is found in the volume column or if 'factor' is invalid.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Validate that required columns exist and factor is valid
            expected_columns = {'name', 'volume'}
            if not all(col in reader.fieldnames for col in expected_columns):
                raise ValueError(f"Input CSV must contain the following columns: {expected_columns}")
            
            if factor <= 0:
                raise ValueError("Scaling factor must be a positive number.")

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['name', 'volume'])
            writer.writeheader()

            for row in reader:
                try:
                    original_volume = float(row['volume'])
                    scaled_volume = round(original_volume * factor, 4) # Round to avoid floating point noise issues like 0.123999999
                    new_row = {'name': row['name'], 'volume': str(scaled_volume)}
                    writer.writerow(new_row)
                except ValueError:
                    raise ValueError(f"Invalid volume value '{row['volume']}' found in input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external files.
    # Simulating a temporary process where the 'sample_data.csv' is created in memory logic, 
    # but since we cannot create pre-existing files on disk during runtime execution of this script alone 
    # (as per "no pre-existing files" constraint implying no dependency on them), 
    # we will generate the input data programmatically and write it to a temporary file path.
    
    import tempfile
    
    sample_data = [
        {'name': 'Apple', 'volume': 0.15},
        {'name': 'Banana', 'volume': 0.28},
        {'name': 'Orange', 'volume': 0.34},
        {'name': 'Milk', 'volume': 1.0}
    ]

    # Create a temporary file to act as the input source since we cannot rely on pre-existing files
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_input:
        writer = csv.DictWriter(temp_input, fieldnames=['name', 'volume'])
        writer.writeheader()
        for item in sample_data:
            writer.writerow(item)
        
        input_path = temp_input.name

    # Define output path and scaling factor
    output_path = "scaled_output.csv"
    user_factor = 2.5
    
    try:
        scale_volumes(input_path, output_path, user_factor)
        print(f"Processing complete. Output saved to {output_path}")
        
        # Clean up temporary input file immediately after use
        import os
        os.remove(input_path)
    except Exception as e:
        print(f"An error occurred during processing: {e}")