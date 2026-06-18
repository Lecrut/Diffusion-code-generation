import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volumes by the given factor,
    and writes the results to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        factor (float): The scaling factor for volume values.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        # Determine fieldnames from the header row
        fieldnames = list(reader.fieldnames) if reader.fieldnames else []

        rows_to_write = []
        for row in reader:
            try:
                original_volume_str = str(row.get('volume', '0'))
                volume = float(original_volume_str.strip())
                
                # Scale the volume
                scaled_volume = round(volume * factor, 2)
                
                # Create a new dictionary with updated values
                new_row = row.copy()
                if fieldnames and 'volume' in fieldnames:
                    new_row['volume'] = str(scaled_volume)
                rows_to_write.append(new_row)
            except ValueError as e:
                print(f"Warning: Skipping invalid volume value '{original_volume_str}' due to {e}")

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows_to_write:
            writer.writerow(row)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external files.
    # We create a temporary directory structure implicitly by writing directly to standard output logic,
    # but since we cannot write to arbitrary paths reliably in all environments without checking existence,
    # and the task forbids pre-existing file dependencies, 
    # we will simulate the process using an in-memory list that is then written to a specific filename.
    
    # To strictly adhere to "no pre-existing files" while needing output:
    # We define input data as strings within this block, read them into memory (simulating reading),
    # and write directly to a fixed path which will be created by the OS if it doesn't exist.
    # However, to avoid file I/O errors on restricted environments during testing without actual files:
    # We will use standard library tempfile logic implicitly or just define the input data explicitly 
    # as strings in memory and write them out. 
    
    # Let's create a temporary filename that is guaranteed unique if we could generate it, 
    # but since we can't call random module for temp names easily without imports (which are fine),
    # let's stick to fixed paths assuming the environment allows creation of new files.
    
    input_data_content = """item_name,volume
Apple,100
Banana,250
Cherry,75"""

    import io
    
    # Create a string buffer acting as our "input file" in memory for this specific run logic
    input_buffer = io.StringIO(input_data_content)
    
    # Read from the virtual input source to simulate reading a CSV
    reader = csv.DictReader(input_buffer)
    fieldnames = list(reader.fieldnames) if reader.fieldnames else []

    scaled_rows = []
    for row in reader:
        try:
            volume_str = str(row.get('volume', '0'))
            volume = float(volume_str.strip())
            
            # User-defined factor is hard-coded here as per task requirements (no args)
            user_factor = 2.5
            
            scaled_volume = round(volume * user_factor, 2)
            
            new_row = row.copy()
            if fieldnames and 'volume' in fieldnames:
                new_row['volume'] = str(scaled_volume)
            scaled_rows.append(new_row)
        except ValueError as e:
            print(f"Warning: Skipping invalid volume value '{volume_str}'")

    # Output to a specific file path. Since we are creating it, no pre-existing file is required.
    output_filename = "scaled_volumes.csv"
    
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in scaled_rows:
            writer.writerow(row)

    print(f"Processing complete. Output written to {output_filename}")