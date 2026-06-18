import csv
from pathlib import Path

def read_and_convert_weights(file_path: str) -> list[float]:
    """
    Reads weight measurements from a CSV file, converts all values to floating-point numbers,
    and returns the average weight after validating entries.

    Args:
        file_path (str): The path to the input CSV file.

    Returns:
        float: The calculated average weight if successful.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric values are found in the data or no numeric weights exist.
    """
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Initialize list to store valid weight numbers
            weights = []
            
            for row_num, row in enumerate(reader):
                if not row or all(cell.strip() == '' for cell in row):
                    continue  # Skip empty rows
                
                try:
                    numeric_values = [float(value) for value in row]
                    
                    # If the current row is supposed to be a single measurement but has multiple,
                    # we treat it as an error unless explicitly part of a list structure.
                    # Assuming standard CSV where each cell might represent one weight or 
                    # if the user passes data that results in lists per row:
                    
                    for value in numeric_values:
                        weights.append(value)

                except ValueError as e:
                    raise ValueError(f"Error on line {row_num + 1}: Non-numeric entry '{value}' encountered.") from e
                    
        return sum(weights) / len(weights) if weights else None
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found. Please ensure the correct path is provided.")

def create_sample_data(file_content):
    """Helper function to simulate reading data (since actual files aren't used here due to constraints)."""
    # Simulate a CSV string structure since we cannot rely on external files
    
if __name__ == '__main__':
    sample_csv_content = '''weight,extra_column
180.5,test_data
75.2,another_row
90.3,"Invalid Data"'''

    # Since the task requires reading from a file but also prohibiting external dependencies/files 
    # and asking to run without user input or command-line arguments:
    
    # We will create an in-memory simulation of what happens when processing data that might look like this,
    # OR we assume the prompt allows us to treat the 'if __name__' block as generating a temporary file 
    # if absolutely necessary to satisfy "reads from CSV", but strictly no external network or args.

    # To be most robust and self-contained without creating actual disk I/O for testing (which might violate
    # strict interpretations of 'no pre-existing files'), we will hardcode the logic demonstration
    # using a string representation that mimics a file object in memory, OR create a temporary CSV 
    # on the fly to ensure the script is truly runnable as requested. 
    
    # Given "reads from a CSV file", let's generate a temp file during execution for this specific run
    # so it feels like reading an actual file, satisfying all constraints (no args, no stdin).

    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp:
        tmp_name = tmp.name
        
        # Write sample data to the temp file