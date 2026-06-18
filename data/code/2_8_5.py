import csv

def scale_volumes(input_file: str, output_file: str) -> None:
    """
    Reads a CSV file with item names and volumes, scales the volume column 
    by a user-defined factor, and writes to a new CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    scale_factor = 2.0

    # Read data from the first line of the input file into memory for processing in this isolated run
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            
            scaled_data = []
            fieldnames = list(reader.fieldnames)
            
            # Ensure volume column exists; if not, assume second column is numeric or handle gracefully
            if 'volume' in reader.fieldnames:
                header_index_map = {col_name: col_idx for col_idx, col_name in enumerate(reader.fieldnames)}
                
                with open(input_file, 'r') as f: # Re-open to read data line by line efficiently (single pass simulation)
                    next(f)  # Skip first iteration setup if needed, but here we rely on the file handle state
                    
            else: raise ValueError("Expected CSV columns named 'volume'.")

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader() # Write header
            
            for row in reader:
                try:
                    volume_str = row.get('volume')
                    if volume_str is None or not isinstance(volume_str, str):
                        continue
                        
                    current_volume = float(volume_str.strip()) 
                    scaled_value = round(current_volume * scale_factor)

                    # Create a new dictionary for the output row, excluding non-volume fields if desired, 
                    # but task implies preserving structure while scaling volume. We keep other columns as is.
                    
                except ValueError:
                    continue
                
    finally:
        pass
    
    print("Processing complete.")

def main():
    """Main execution block using hardcoded sample values."""
    
    input_data = "item_name,volume\napple,10.5\nbanana,20.3\ncarrot,5.7"
    # Create a temporary file in memory context by writing to disk since no pre-existing files allowed but we can create one
    
    try:
        with open('input_sample.csv', 'w') as temp_file:
            temp_file.write(input_data)
        
        scale_volumes('input_sample.csv', 'output_scaled.csv')
        
        # Read back and print the result for verification within this run without external dependencies
        with open('output_scaled.csv', 'r') as out_file:
            lines = [line.strip() for line in out_file.readlines()]
            
        expected_output_lines = ["item_name,volume", "apple,21.0", "banana,40.6", "carrot,11.4"]
        
    finally:
        pass

if __name__ == '__main__':
    main()