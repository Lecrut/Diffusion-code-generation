import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 'factor',
    and writes the results to a new CSV file.

    Args:
        input_file (str): Path to the source CSV file. Expected columns are 'name' and 'volume'.
        output_file (str): Path to the destination CSV file where scaled data will be saved.
        factor (float): The multiplication factor for scaling volumes.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a volume cannot be converted to float or if 'volume' column is missing.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Verify that the expected columns exist
        required_columns = {'name', 'volume'}
        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(f"Input file must contain columns {required_columns}, found: {reader.fieldnames}")

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['name', 'scaled_volume'])
            
            # Write header (using a new column name for the scaled value)
            writer.writeheader()

            for row in reader:
                try:
                    original_volume = float(row['volume'])
                    scaled_value = original_volume * factor
                    writer.writerow({'name': row['name'], 'scaled_volume': f"{scaled_value:.2f}"})
                except ValueError as e:
                    raise ValueError(f"Invalid volume value '{row.get('volume', '')}' for item '{row.get('name')}'.") from e

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external files.
    # This block creates a temporary source file in memory logic (simulated via string) 
    # and writes directly to an output, but since we cannot create pre-existing files on disk 
    # for this specific constraint ("no pre-existing files"), we will simulate the read/write process
    # by defining the data inline within the function call or creating a temporary file path.
    
    # To strictly adhere to "run without user input... or pre-existing files", 
    # and since we cannot guarantee disk write permissions on all environments for temp files,
    # we will create a small script that defines the CSV content as strings and writes it out.
    # However, the task asks to read a CSV file. Since no such file exists initially:
    # We will use a temporary file approach which is standard for "no pre-existing files" constraints 
    # in Python scripts unless 'tempfile' module usage is restricted (it isn't).
    
    import tempfile
    
    source_data = """name,volume
Apple,10.5
Banana,23.4
Cherry,8.9"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_src:
        temp_name = temp_src.name
        # Write sample data to the temporary file
        writer = csv.writer(temp_src)
        writer.writerow(['name', 'volume'])
        writer.writerow(['Apple', 10.5])
        writer.writerow(['Banana', 23.4])
        writer.writerow(['Cherry', 8.9])

    # Define output file path (also temporary to avoid polluting the directory)
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_dst:
        dest_name = temp_dst.name

    try:
        scale_volumes(temp_name, dest_name, factor=2.0)
        
        # Print confirmation and content of the output file to verify success without external prompts
        print(f"Processing complete.")
        print(f"Source processed from: {temp_name}")
        print(f"Output written to: {dest_name}")
        
        with open(dest_name, 'r') as f:
            content = f.read()
            print("Generated Output Content:")
            print(content)

    finally:
        # Clean up temporary files created during execution
        import os
        if os.path.exists(temp_name):
            os.remove(temp_name)
        if os.path.exists(dest_name):
            os.remove(dest_name)