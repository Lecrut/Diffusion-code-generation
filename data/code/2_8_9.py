import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volumes by the given factor,
    and writes the results to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file containing 'item_name' and 'volume'.
        output_file (str): Path to the output CSV file where scaled data will be saved.
        factor (float): The scaling factor for volumes.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Verify expected columns exist
            if 'item_name' not in reader.fieldnames or 'volume' not in reader.fieldnames:
                raise ValueError("Input CSV must contain 'item_name' and 'volume' columns.")

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['item_name', 'scaled_volume'])
                
                for row in reader:
                    try:
                        original_volume = float(row['volume'])
                        scaled_value = original_volume * factor
                        
                        # Write output with a key named 'scaled_volume' as per task logic
                        writer.writerow({
                            'item_name': row['item_name'],
                            'scaled_volume': f"{scaled_value:.6f}"  # Format for consistency
                        })
                    except ValueError:
                        raise ValueError(f"Invalid volume value found in row {row}: '{row['volume']}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external files.
    # We create a temporary in-memory structure to simulate reading, but since the task 
    # requires processing an existing file format and outputting to one, we will use 
    # standard library features to generate a minimal valid CSV string on the fly if needed?
    # However, strict adherence says "Do not include ... pre-existing files". 
    # To satisfy this while providing runnable code that processes data:
    # We can define the input content directly in memory and write it to a temp file path 
    # or simply process a string buffer. But the task asks for reading a CSV file.
    
    # Since we cannot rely on pre-existing files, let's create them dynamically within this block?
    # No, "pre-existing files" usually refers to dependencies like config.json in project root.
    # Creating temporary files during execution is generally acceptable unless forbidden explicitly.
    # To be safest and most robust without any file I/O dependency at all (except the output):
    
    import tempfile
    
    sample_data_content = """item_name,volume
Apple,100
Banana,250
Cherry,75"""

    input_filename = "sample_input.csv"
    output_filename = "scaled_output.csv"
    scaling_factor = 2.5

    # Create a temporary file to hold the sample data so we can read it as requested 
    # without requiring an external pre-existing file in the environment.
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_input:
        tmp_input.write(sample_data_content)
        temp_path = tmp_input.name

    try:
        scale_volumes(temp_path, output_filename, scaling_factor)
        
        # Print confirmation of success (optional but good for verification)
        print(f"Processing complete. Output written to {output_filename}")
    finally:
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)