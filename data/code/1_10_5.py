import csv
from pathlib import Path

def parse_weight_file(file_path: str) -> list[float]:
    """Reads a CSV file, extracts weight values from numeric columns or rows,
    converts them to floats, and handles non-numeric entries gracefully."""
    
    weights = []
    
    # Verify the path exists before attempting to read
    if not Path(file_path).exists():
        raise FileNotFoundError(f"The specified file '{file_path}' does not exist.")

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip empty lines or malformed rows that don't have data
            for row in reader:
                if not row or all(cell.strip() == '' for cell in row):
                    continue
                
                try:
                    # Attempt to convert the entire row as a single float first (e.g., "10.5")
                    weights.append(float(row[0]))
                except ValueError:
                    # If that fails, attempt individual cells if there are multiple columns
                    for cell in row:
                        try:
                            val = float(cell)
                            # Avoid duplicates if the same value appears twice (optional robustness)
                            if not weights or abs(val - weights[-1]) > 0.0001: 
                                weights.append(val)
                        except ValueError:
                            continue
                
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{file_path}'.")
    except csv.Error as e:
        raise RuntimeError(f"CSV parsing error occurred: {e}")

    return weights

def calculate_average(weights: list[float]) -> float | None:
    """Calculates the average of a list of floats. Returns None if empty."""
    if not weights:
        return None
    
    total = sum(weights)
    return total / len(weights)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external files or user input
    sample_csv_content = """weight,age,height
75.0,25,180
68.5,30,175
invalid_data,40,190
72.3,,185"""

    # Create a temporary file in memory simulation by writing to disk then deleting immediately? 
    # No, the requirement says "pre-existing files" are not allowed and sample must run without user input.
    # We will simulate reading from a string buffer that mimics CSV behavior or write to temp and delete.
    # To be strictly robust as per "no pre-existing files", we can create a temporary file in the same process, 
    # but since standard `input()` is banned, creating a temp file dynamically is acceptable for testing logic.
    
    import tempfile
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            tmp_file.write(sample_csv_content)
            tmp_path = tmp_file.name
        
        # Parse the weights from our temporary file
        weight_data = parse_weight_file(tmp_path)
        
        if not weight_data:
            print("No valid numeric data found.")
            average_result = None
        else:
            avg_weight = calculate_average(weight_data)
            
            if avg_weight is not None:
                # Filter out 'invalid' entries that might have been parsed incorrectly or handle them? 
                # The prompt says "ensuring error handling for non-numeric entries". 
                # Our parse function skips invalid cells. Let's verify what we got.
                
                print(f"Parsed weights: {weight_data}")
                if avg_weight is not None:
                    print(f"Average weight: {avg_weight:.2f} kg")
            else:
                print("Failed to calculate average.")

    finally:
        # Clean up the temporary file created for testing purposes
        try:
            Path(tmp_path).unlink()
        except FileNotFoundError:
            pass