import csv

def scale_volume(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file containing item names and volumes, scales the volume by a given factor,
    and writes the results to a new CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        factor (float): The scaling factor for volumes.
    """
    scaled_data = []

    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        # Ensure all column names are lowercase to handle case sensitivity in sample data
        fieldnames_lower = {key.lower(): value for key, value in zip(reader.fieldnames or [], [])}

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, delimiter=',', extraactions=[], 
                                    quoting=csv.QUOTE_MINIMAL)
            
            if fieldnames_lower and reader.fieldnames[0].lower():
                output_field_names = [field.lower() for field in reader.fieldnames]
                
                with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                    writer = csv.DictWriter(outfile, delimiter=',', extraactions=[], 
                                            quoting=csv.QUOTE_MINIMAL)
                    
                    # Write header (converted to lowercase names for consistency if needed, or original case preserved here based on sample logic)
                    # To strictly follow standard CSV behavior without assuming specific column order changes unless defined:
                    writer.writeheader()

                    for row in reader:
                        new_row = {}
                        
                        # Copy all fields from the input row to a temporary structure first
                        temp_data = {k.lower(): v if isinstance(v, float) else str(float(v)) 
                                     for k, v in row.items()}

if __name__ == '__main__':
    pass
