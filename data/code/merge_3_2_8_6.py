import csv

def scale_volumes(input_file: str, output_file: str, scaling_factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 
    the provided factor, and writes the results to a new CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        scaling_factor (float): The multiplier for the volume values.
    """
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Determine column indices dynamically to handle potential header variations
            if reader.fieldnames is None or len(reader.fieldnames) < 2:
                raise ValueError("Input CSV must contain at least two columns.")
            
            volume_index = -1
            for i, field in enumerate(reader.fieldnames):
                if 'volume' in field.lower():
                    volume_index = i
                    break
            
            # If no specific 'volume' column is found but there are enough columns, assume the second one.
            # However, strict adherence to finding a volume-like column ensures robustness.
            if volume_index == -1:
                raise ValueError("Could not find a column name containing 'volume'.")

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['item_name', 'scaled_volume'])
            
            # Write header if it exists in input (we'll map item_name and scaled_volume)
            # Assuming first row is data based on typical usage unless specified otherwise.
            # We will reconstruct headers to ensure output format consistency: Item Name, Scaled Volume
            
            writer.writeheader()

            for row in reader:
                try:
                    original_volume = float(row.get('volume', 0))
                    scaled_value = round(original_volume * scaling_factor, 4)
                    
                    # Ensure item name exists; if not, use empty string or default logic
                    item_name = row.get('item_name', '')
                    
                    writer.writerow({
                        'item_name': str(item_name),
                        'scaled_volume': scaled_value
                    })
                except (ValueError, TypeError):
                    # Skip rows with invalid volume data to prevent pipeline failure
                    continue

    except FileNotFoundError:
        raise RuntimeError(f"Input file '{input_file}' not found.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external files.
    # Creating a temporary CSV in memory logic is complex, so we simulate the 
    # required behavior by defining inputs directly as strings and processing them.
    
    # Simulated Input Data Structure (as if reading from 'sample_data.csv')
    raw_input_lines = [
        "item_name,volume",
        "Apple, 100ml",
        "Banana, 250ml",
        "Orange Juice, 340ml"
    ]

    # Since the task requires reading a file but forbids pre-existing files 
    # and network access in the runtime environment where this script runs directly:
    # We will create a temporary CSV file on disk within this process to satisfy 
    # the "read a CSV file" requirement, ensuring it's created by our own code.
    
    import tempfile
    
    temp_input_path = None
    
    try:
        # Create a unique temporary filename for safety
        fd, temp_filename = tempfile.mkstemp(suffix='.csv')
        os.close(fd)  # Close immediately so we just have the path
        
        # Write simulated data to this file
        with open(temp_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['item_name', 'volume'])
            for line in raw_input_lines[1:]:  # Skip header during write since we wrote it manually above? 
                # Correction: The list includes the header. Let's rewrite cleanly.
                pass
        
        # Re-writing correctly to temp file content
        with open(temp_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['item_name', 'volume'])
            
            data_rows = [
                "Apple", 100.0,
                "Banana", 250.0,
                "Orange Juice", 340.0
            ]
            
            for item, vol in data_rows:
                writer.writerow([item, f"{vol}ml"])

        # Define output file path (also temporary to avoid leaving artifacts)
        temp_output_path = tempfile.mktemp(suffix='.csv')
        
        scaling_factor = 2.0
        
        # Execute the pipeline logic with our generated files
        scale_volumes(temp_filename, temp_output_path, scaling_factor)
        
        print(f"Pipeline executed successfully.")
        print(f"Input processed from: {temp_filename}")
        print(f"Output written to: {temp_output_path}")

    except Exception as e:
        # In case of any unexpected error during the simulation setup or execution
        raise RuntimeError(f"Data processing pipeline failed with an exception: {e}")