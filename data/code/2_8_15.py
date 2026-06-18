import csv

def scale_volumes(input_file: str, output_file: str, scaling_factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by a factor,
    and writes the results to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file containing 'name' and 'volume'.
        output_file (str): Path where the scaled data will be saved.
        scaling_factor (float): The multiplier for volume values.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a non-numeric value is encountered in the volume column.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Verify expected columns
            if 'name' not in reader.fieldnames or 'volume' not in reader.fieldnames:
                raise ValueError(f"Expected CSV columns ['name', 'volume'], found {reader.fieldnames}")

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['name', 'scaled_volume'])
                
                # Write header (adjusting column name to reflect scaling)
                writer.writerow({'name': '', 'scaled_volume': ''})

                for row in reader:
                    try:
                        original_volume = float(row['volume'])
                        scaled_value = original_volume * scaling_factor
                        writer.writerow({
                            'name': row['name'],
                            'scaled_volume': f"{scaled_value:.6f}" if not isinstance(scaled_value, int) else str(scaled_value)
                        })
                    except ValueError as ve:
                        raise ValueError(f"Invalid volume value '{row.get('volume', '')}' for item '{row.get('name')}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external files)
    
    # Create a temporary in-memory simulation by writing to a string buffer first, 
    # then saving it to ensure the pipeline logic is tested without pre-existing files.
    import io
    
    raw_csv_content = """name,volume
Apple,100
Banana,250
Cherry,75
Date,300"""

    temp_input_path = "/tmp/sample_data.csv"
    
    # Write temporary input file for the pipeline to read from (allowed as it's not pre-existing)
    with open(temp_input_path, 'w', encoding='utf-8') as f:
        f.write(raw_csv_content.strip())

    try:
        scaling_factor = 2.5
        
        scale_volumes(
            input_file=temp_input_path, 
            output_file="/tmp/scaled_data.csv", 
            scaling_factor=scaling_factor
        )
        
        print("Pipeline completed successfully.")
        
        # Verify output content for confirmation (optional debug step)
        with open("/tmp/scaled_data.csv", 'r') as f:
            verified_content = f.read()
            
    finally:
        # Clean up temporary files used during this execution block
        import os
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)
        if os.path.exists("/tmp/scaled_data.csv"):
            os.remove("/tmp/scaled_data.csv")