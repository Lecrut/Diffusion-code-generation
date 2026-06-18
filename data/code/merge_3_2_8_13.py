import csv

def scale_volumes(input_file: str, output_file: str, factor: float) -> None:
    """
    Reads a CSV file with 'item' and 'volume', scales volumes by `factor`,
    and writes the results to an output CSV.
    
    Args:
        input_file (str): Path to the source CSV file.
        output_file (str): Path to the destination CSV file.
        factor (float): The scaling multiplier for volume values.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        # Write header to output based on original columns + new column if needed, 
        # but task implies just scaling existing data structure. Assuming standard ['item', 'volume'] or similar.
        fieldnames = reader.fieldnames
        
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames)
            writer.writeheader()
            
            for row in reader:
                original_volume = float(row['volume'])
                scaled_volume = original_volume * factor
                
                # Create new row with updated volume. 
                # We keep the same keys but update 'volume'. If input had other keys, they are preserved.
                row_copy = dict(row)
                row_copy['volume'] = str(scaled_volume)
                
                writer.writerow(row_copy)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or network access).
    
    # Define a temporary list to simulate reading from file for the sake of this standalone module logic.
    # In a real scenario, 'sample_data.csv' would exist on disk. 
    # To ensure it runs without pre-existing files in the environment where we generate code:
    # We will write the sample data internally into a temporary string or process a list if file access is risky?
    # The prompt says "output a new file". It implies reading from an input file exists.
    # However, constraint says: "run without... pre-existing files."
    # This creates a conflict: If I need to read 'sample_data.csv', it must exist or be created first.
    # Creating the file inside `if __name__` satisfies the requirement of not requiring *pre-existing* ones at startup time, 
    # but technically modifies the filesystem during execution. 
    # A safer interpretation for "no pre-existing files" is that I should generate a temporary input in memory or create it on the fly?
    # Let's assume we can write to disk temporarily if needed, OR simulate reading via an embedded list and writing output immediately.
    
    # To strictly adhere to "run without... pre-existing files", let's avoid relying on 'sample_data.csv' existing beforehand.
    # We will create a temporary input file in memory (using BytesIO) or just write the logic such that 
    # if the user runs this, we generate a temp file and read it? No, simpler:
    # Just use an embedded list to simulate reading, then write ONLY the output file. This avoids needing any external CSV at all.
    
    sample_data = [
        {'item': 'Apple', 'volume': 10},
        {'item': 'Banana', 'volume': 25},
        {'item': 'Orange', 'volume': 30}
    ]

    # Since we cannot read from a non-existent file, and the task says "read a CSV", 
    # but also forbids pre-existing files for the sample block to run:
    # The most robust solution is to create an input file temporarily within this script execution,
    # process it, then delete it (optional), or just use in-memory processing that mimics reading.
    
    # Let's implement a helper to write the dummy data to a temp file so we can demonstrate 
    # the "read CSV" functionality as requested, ensuring no external dependency is needed at startup.
    
    import tempfile
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_in:
            writer = csv.DictWriter(tmp_in.fieldnames if hasattr(csv.writer(tmp_in), 'fieldnames') else None) # Trick to get fieldnames? 
            # Actually easier: manually write header and rows.
            
            content_lines = ['item,volume\n']
            for item in sample_data:
                line = f"{item['item']},{int(item['volume'])}\n"
                content_lines.append(line)
            
            tmp_file_path = tempfile.mktemp(suffix='.csv')
            with open(tmp_file_path, 'w', newline='', encoding='utf-8') as tf:
                tf.writelines(content_lines)

        # Now we have a valid input file created dynamically.
        scale_volumes(input_file=tmp_file_path, output_file='scaled_output.csv', factor=2.0)
        
    finally:
        try:
            os.remove(tmp_file_path) if 'tmp_file_path' in locals() else None 
        except FileNotFoundError:
            pass

# Wait, I need to import `os` for removal and ensure clean execution without side effects being flagged as "pre-existing".
# Actually, creating a file during runtime is fine. The constraint is "no pre-existing files" at the moment of running interpretation?
# Or does it mean no input arguments pointing to existing files? 
# Let's refine: Just create everything in memory if possible, but the function signature expects file paths.
# To make `scale_volumes` work without an actual external CSV being present *before* execution:
    # I will use a BytesIO object or similar for reading inside scale_volumes to avoid disk dependency entirely? 
    # But the task says "read a CSV file... output a new file". It implies filesystem interaction is desired.
    
    # Revised plan for `if __name__`:
    # 1. Create a temp input file with sample data (satisfies no pre-existing requirement).
    # 2. Call scale_volumes to read that and write 'scaled_output.csv'.
    # 3. Clean up the temp input file immediately after processing.

# Need `os` import for cleanup? Yes, but imports are allowed at top level if needed? 
# "Return only a single complete runnable Python module." -> Imports can be anywhere really, usually top is standard.
# However, to minimize external dependencies beyond csv/os:

import os

if __name__ == '__main__':
    # Sample data embedded directly
    sample_rows = [
        {'item': 'Apple', 'volume': 10},
        {'item': 'Banana', 'volume': 25},
        {'item': 'Orange', 'volume': 30}
    ]

    temp_input_path = None
    
    try:
        # Create a temporary input file dynamically to satisfy "read CSV" without pre-existing files requirement.
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp_file:
            tmp_file_path = tmp_file.name
            
            writer = csv.writer(tmp_file)
            writer.writerow(['item', 'volume']) # Write header
            for row in sample_rows:
                writer.writerow([row['item'], int(row['volume'])])

        # Now execute the pipeline logic on this temporary file.
        scale_volumes(input_file=tmp_file_path, output_file='scaled_output.csv', factor=2.0)
        
    finally:
        if temp_input_path and os.path.exists(temp_input_path):
            try:
                os.remove(temp_input_path)
            except OSError:
                pass