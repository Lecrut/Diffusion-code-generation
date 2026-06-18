import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 'factor',
    and writes the results to the specified output file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the new output CSV file.
        factor (float): The multiplier for scaling volumes.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If volume values are non-numeric or negative where not expected.
    """
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Verify that the CSV has headers containing both name and volume indicators
            if reader.fieldnames is None or ('name' not in [f.lower() for f in reader.fieldnames] 
                                       or 'volume' not in [f.lower() for f in reader.fieldnames]):
                raise ValueError("Input CSV must contain columns named 'name' and 'volume'.")

            # Write the header to the output file immediately
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                
                for row in reader:
                    original_volume_str = row['volume'].strip()
                    
                    # Attempt to parse the volume value
                    try:
                        original_volume = float(original_volume_str)
                    except ValueError as e:
                        raise ValueError(f"Invalid numeric volume found at {row.get('name', 'unknown')}: '{original_volume_str}'") from e
                    
                    if original_volume < 0:
                        # Assuming volumes are physical quantities, negative values are invalid input for scaling logic generally
                        raise ValueError(f"Non-positive volume value {original_volume} found in row for item '{row['name']}'. Cannot scale.")
                    
                    scaled_volume = original_volume * factor
                    
                    # Update the dictionary with calculated value and write to file (or keep as dict)
                    if 'volume' not in writer.fieldnames:
                        raise ValueError("Output CSV must include a column named 'volume'.")

                    row['volume'] = str(scaled_volume)  # Convert back to string for writing
                    writer.writerow(row)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

if __name__ == '__main__':
    # Hard-coded sample values meeting all constraints (no input(), sys.stdin, etc.)
    
    # Create a temporary dummy input structure in memory for demonstration if needed, 
    # but the task implies reading an existing file. Since no pre-existing files are allowed,
    # we will simulate the logic using hardcoded data written to a strict local path that does not exist initially.
    # To strictly adhere to "no pre-existing files", this script generates its own input content 
    # by writing it first (allowed in memory generation context or immediate filesystem write if target dir exists),
    # but typically for such tasks, we assume the directory structure might be created or just use a standard approach.
    
    # Since I cannot guarantee an existing file 'sample_data.csv' on every runner without creating one locally first:
    # I will implement logic that creates the input CSV from scratch within this block if it's missing? 
    # No, "Do not include ... pre-existing files" usually means don't rely on them being there.
    # However, to make a single runnable module self-contained without external dependencies or network access:
    
    # Strategy: Write the sample input file first (creating a new one is fine), then process it.
    
    import os
    
    SAMPLE_INPUT_FILE = 'sample_data.csv'
    OUTPUT_FILE = 'scaled_output.csv'
    SCALE_FACTOR = 10.5
    
    # Check if input exists, if not, create the sample data file to ensure execution works in a clean environment.
    if not os.path.exists(SAMPLE_INPUT_FILE):
        with open(SAMPLE_INPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['item_name', 'volume']) # Header must match expected logic or be flexible? 
            # The task says "read a CSV file containing item names and their corresponding volumes". It doesn't specify strict headers.
            # Let's stick to the generic DictReader expectation which checks for presence of name/volume keys.
            
        # Sample Data Rows
        sample_items = [
            {"item_name": "Apple", "volume": 50},
            {"item_name": "Watermelon", "volume": 200},
            {"item_name": "Lemonade", "volume": 175.5}
        ]
        
        for item in sample_items:
            writer.writerow([str(item['item_name']), str(item['volume'])])

    # Execute the processing pipeline with user-defined factor (hard-coded)
    scale_volumes(SAMPLE_INPUT_FILE, OUTPUT_FILE, SCALE_FACTOR)
    
    print(f"Successfully processed {SAMPLE_INPUT_FILE} -> {OUTPUT_FILE}")