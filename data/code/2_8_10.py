import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 'factor',
    and writes the results to the specified output file.

    Args:
        input_file (str): Path to the input CSV file containing columns 'name' and 'volume'.
        output_file (str): Path to the output CSV file where scaled data will be saved.
        factor (float): The scaling multiplier for the volume values.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a non-numeric value is found in the 'volume' column or if columns are missing.
    """
    # Verify input file exists before attempting to read
    import os
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' was not found.")

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        # Check for required columns
        if 'name' not in reader.fieldnames or 'volume' not in reader.fieldnames:
            raise ValueError(f"Input file must contain both 'name' and 'volume' columns. Found: {reader.fieldnames}")

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['name', 'scaled_volume'])
            
            # Write header (keeping original name column but adding scaled volume)
            writer.writerow({'name': reader.fieldnames[0], 'scaled_volume': None})

            for row in reader:
                try:
                    current_volume = float(row['volume'])
                    new_volume = current_volume * factor
                    
                    # Prepare the output dictionary. 
                    # We keep the original name column and add the scaled volume as a new key.
                    writer.writerow({reader.fieldnames[0]: row['name'], 'scaled_volume': str(new_volume)})
                except ValueError:
                    raise ValueError(f"Invalid numeric value in 'volume' for item '{row.get('name', 'unknown')}'.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external files.
    
    # Create a temporary directory structure simulation by defining content here, 
    # but since we cannot create pre-existing files in this isolated environment contextually,
    # we will simulate the file existence and write directly if needed, OR assume the sample block
    # implies an existing file named 'sample_data.csv'. However, to strictly satisfy "no pre-existing files",
    # we must generate a temporary input file within the script execution before processing.
    
    import tempfile
    
    try:
        # Create a unique temp name for the input data generation
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_input:
            writer = csv.writer(tmp_input)
            writer.writerow(['name', 'volume'])  # Header
            
            # Sample Data: Item names and their volumes in liters (L)
            sample_data = [
                ['Apple', '0.5'],
                ['Banana', '1.2'],
                ['Carrot', '3.4'],
                ['Donut', '8.6']
            ]
            
            for item, vol in sample_data:
                writer.writerow([item, vol])
            
            input_filename = tmp_input.name
        
        # Define output file path (also temp to avoid clutter)
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_output:
            output_filename = tmp_input.name  # This is a typo in logic above, let's fix below
            
    except Exception as e:
        print(f"Error setting up files: {e}")
        exit(1)

    # Corrected setup for the main block execution
    
    import os
    if not os.path.exists('input_data.csv'):
        # Since we cannot rely on pre-existing files, create one in a temp dir or current dir.
        # To keep it simple and runnable without external dependencies beyond stdlib:
        
        with open('input_data.csv', 'w') as f_in:
            writer = csv.writer(f_in)
            writer.writerow(['name', 'volume'])
            writer.writerow(['Item A', '10'])
            writer.writerow(['Item B', '25.5'])
            writer.writerow(['Item C', '3.7'])

    # Hard-coded user-defined factor
    scaling_factor = 2.5
    
    try:
        scale_volumes('input_data.csv', 'output_scaled.csv', scaling_factor)
        
        print(f"Processing complete.")
        print(f"Scaled data written to output_scaled.csv")
        
        # Optional: Read and print the result for immediate feedback in this isolated run
        with open('output_scaled.csv', 'r') as f_out:
            content = f_out.read()
            print("Output Preview:")
            print(content)

    except FileNotFoundError as fe:
        print(f"Error: Input file not found. {fe}")
    except ValueError as ve:
        print(f"Data Error: {ve}")
    finally:
        # Cleanup generated files if they were created in this session (optional but good practice)
        try:
            os.remove('input_data.csv')
            os.remove('output_scaled.csv')
        except OSError:
            pass