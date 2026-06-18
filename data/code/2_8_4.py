import csv

def scale_volumes(input_path: str, output_path: str, scale_factor: float) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column by 
    a factor, and writes the results to a new CSV file.
    
    Args:
        input_path (str): Path to the source CSV file.
        output_path (str): Path to the destination CSV file.
        scale_factor (float): The multiplication factor for volumes.
    """
    try:
        with open(input_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Prepare headers and data for output
            fieldnames = list(reader.fieldnames) + ['scaled_volume']
            rows = []
            
            for row in reader:
                try:
                    original_volume = float(row['volume']) * scale_factor
                    scaled_row = dict(row)
                    scaled_row['scaled_volume'] = round(original_volume, 2)
                    rows.append(scaled_row)
                except ValueError as e:
                    print(f"Warning: Invalid volume value '{row.get('volume')}' for item {row.get('name', 'unknown')}")

        with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    # Simulating reading from a temporary in-memory structure directly for demonstration, 
    # but structuring the call as if processing an existing file path pattern.
    
    # Define mock data content that would normally be in 'sample_data.csv'
    sample_content = """name,volume
Apple,0.5kg
Banana,1.2kg
Orange,0.3kg"""

    # Create a temporary input file to satisfy the logic flow of reading and writing new files.
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_in:
        tmp_in.write(sample_content)
        temp_input_path = tmp_in.name
        
    output_file_name = 'scaled_output.csv'

    # Execute the pipeline scaling by a user-defined factor of 2.5x
    scale_factor = 2.5
    
    scale_volumes(temp_input_path, output_file_name, scale_factor)
    
    print(f"Pipeline completed successfully.")
    print("Scaled data written to:", output_file_name)