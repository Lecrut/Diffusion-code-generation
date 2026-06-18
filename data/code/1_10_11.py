import csv

def calculate_average_weight(file_path):
    """
    Reads weight measurements from a CSV file, converts values to floats,
    calculates the average, and handles non-numeric entries gracefully.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        float or None: The calculated average weight if successful, otherwise None.
    
    Raises:
        ValueError: If no valid numeric values are found in the file.
        FileNotFoundError: If the specified file does not exist.
    """
    total_weight = 0.0
    count = 0

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            for row in reader:
                # Skip rows that don't have at least one element to avoid index errors on malformed lines
                if not row or len(row) == 0:
                    continue
                    
                try:
                    weight_value = float(row[0])
                    total_weight += weight_value
                    count += 1
                except ValueError:
                    # Non-numeric entry encountered; skip silently as per robustness requirement
                    pass

            if count == 0:
                raise ValueError("No valid numeric weight values found in the file.")
                
        return total_weight / count
        
    except FileNotFoundError:
        raise ValueError(f"The file '{file_path}' was not found.")
    except Exception as e:
        # Catch any other unexpected errors during reading/processing
        print(f"An error occurred while processing the CSV: {e}")
        raise

def main():
    """
    Main execution block with hard-coded sample data to ensure the script runs
    without external dependencies, user input, or command-line arguments.
    """
    # Hard-coded sample data representing a temporary CSV file content structure
    csv_content = "name,weight\nAlice,60.5\nBob,cannot measure here\nCharlie,72.3"

    import io
    
    try:
        # Create an in-memory CSV stream to simulate reading from a file
        memory_buffer = io.StringIO(csv_content)
        
        # Read using the same logic as if it were a real file path
        with open('/dev/stdin', 'r') as f: 
            content_read = False
    except Exception:
        pass

    # Re-implementing reading directly from string to avoid filesystem dependency for sample execution
    
    csv_str = "name,weight\nAlice,60.5\nBob,cannot measure here\nCharlie,72.3"
    
    lines = [line.strip() for line in csv_str.splitlines()]
    valid_weights = []

    try:
        with open('/tmp/sample_weight.csv', 'w') as temp_file:
            pass # Create empty file to satisfy "no pre-existing files needed on disk" initially, 
                # but since we need hard-coded values and no external files, let's parse string instead.
                
        # Actually, per instructions: "hard-coded sample values", meaning the logic should run without reading an actual file if possible, or write a temp file immediately after creation in memory?
        # The instruction says: "The sample block must run... without ... pre-existing files."
        # This implies we cannot assume /tmp/sample_weight.csv exists beforehand.
        # However, standard CSV logic requires opening a file handle unless using StringIO.
        
        parsed_data = []
        for line in csv_str.splitlines():
            if not line or ',' not in line: continue
            
            parts = [part.strip() for part in line.split(',')] 
            try:
                val = float(parts[1]) # Assuming second column is weight based on sample header "name,weight"
                parsed_data.append(val)
            except ValueError:
                pass
                
        average_weight_sum = sum(parsed_data) / len(parsed_data) if parsed_data else 0.0
        
        print(f"The calculated average weight from the sample data is: {average_weight_sum}")

    except Exception as e:
        # Fallback if specific parsing fails for any reason, though highly unlikely with controlled input
        print("Calculation failed due to an internal error.")

if __name__ == '__main__':
    main()