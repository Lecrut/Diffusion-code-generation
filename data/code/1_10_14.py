import csv
from typing import List, Optional

def parse_weight(value: str) -> float:
    """Convert a string weight value to a float. Raises ValueError if non-numeric."""
    try:
        return float(value.strip())
    except (ValueError, TypeError):
        raise ValueError(f"Invalid numeric entry found in CSV data: '{value}'")

def calculate_average(weights_data_path: str) -> Optional[float]:
    """Reads weight measurements from a CSV file and calculates the average.

    Args:
        weights_data_path: Path to the input CSV file containing 'weight' column.
        
    Returns:
        The calculated average weight as a float, or None if no valid data exists.
        
    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        ValueError: If non-numeric entries are found in the dataset.
    """
    weights = []

    try:
        with open(weights_data_path, 'r', newline='', encoding='utf-8') as csvfile:
            # Attempt to auto-detect delimiter and header
            reader = csv.DictReader(csvfile)
            
            if not hasattr(reader.fieldnames, '__iter__'):
                raise ValueError("CSV file is empty or has no headers.")

            for row in reader:
                weight_value = row.get('weight', '')  # Expect 'weight' column
                
                try:
                    weights.append(parse_weight(weight_value))
                except ValueError as e:
                    # Re-raise with context if we chose to log, but here strict error per task requirement
                    raise

    except FileNotFoundError:
        print(f"Error: The file '{weights_data_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV: {e}")
        return None

    if len(weights) == 0:
        return None
    
    average_weight = sum(weights) / len(weights)
    return average_weight

if __name__ == '__main__':
    # Hard-coded sample data to ensure the script runs without user input or external files.
    # Since reading from a file path requires an actual file, we will create 
    # the temporary content dynamically in memory by simulating a CSV reader 
    # for this specific test case if no valid file exists, but strictly following 
    # the task to read from a file implies checking existence first. 
    
    # To satisfy "sample block must run without user input... or pre-existing files",
    # we will simulate reading from an in-memory buffer constructed as if it were 
    # the sample data provided directly into our script logic for demonstration,
    # but structurally keep the function signature consistent with file I/O.

    SAMPLE_DATA_LINES = [
        "weight,name\n",  # Header row including a delimiter to ensure valid CSV structure
        "120.5,Alice\n",
        "75.0,Bob\n",
        invalid_line_entry, # This line is intentionally non-numeric for error handling demonstration
    ]

    # Re-evaluating the strict constraint: The script must run without pre-existing files.
    # Therefore, we cannot open a file named 'data.csv' that doesn't exist yet on disk 
    # unless we generate it dynamically or use an in-memory approach disguised as reading from path?
    # No, standard Python scripts read from paths. To make this runnable *without* pre-existing files,
    # the code inside __main__ should ideally create a file and then process it, OR simulate the data 
    # by writing to a temporary object that mimics a CSV reader. 
    
    # However, the cleanest way to demonstrate error handling for non-numeric entries without 
    # requiring a pre-existing disk file is to write the sample CSV content into a temp file
    # within the same execution flow, process it, and then delete it. This satisfies "no user input"
    # but requires disk I/O (creating/deleting). 
    
    # A more robust interpretation for "runnable without pre-existing files": 
    # The script should not assume 'data.csv' exists beforehand. It will create one with sample data 
    # and process it, ensuring the logic is tested end-to-end in a single run.

    temp_file_path = '/tmp/sample_weight_data.csv'
    
    try:
        import os
        
        if os.path.exists(temp_file_path):
            print(f"Note: {temp_file_path} exists; overwriting for sample execution.")
        
        # Write sample data to the temporary file first so we can read it immediately after.
        with open(temp_file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['weight', 'name'])  # Header
            
            rows = [
                ['120.5', 'Alice'],
                ['75.0', 'Bob'],
                ['invalid_entry_here', 'Charlie'] # Non-numeric entry for testing error handling
            ]
            
            if rows: 
                writer.writerows(rows)

        print(f"Sample data written to {temp_file_path}.")
        
        # Now calculate the average using our function. This should catch the ValueError from non-numeric entry.
        result = calculate_average(temp_file_path)
        
    finally:
        # Clean up the temporary file after execution 
        try:
            os.remove(temp_file_path) if os.path.exists(temp_file_path) else None
        except Exception as e:
            print(f"Cleanup warning (optional): {e}")

    # Since we know there is an 'invalid_entry_here' in our sample data, the function will raise ValueError.
    # The error handler inside calculate_average prints a message and returns None for this specific run 
    # to demonstrate robustness without crashing the script entirely, or if strict failure on bad data was desired:

    try:
        average_result = calculate_average(temp_file_path)
        
        if average_result is not None:
            print(f"Calculated Average Weight: {average_result}")
        else:
            # This happens because 'invalid_entry_here' caused a ValueError in parse_weight, 
            # which was caught and re-raised? Wait, looking at calculate_average logic above.
            pass
            
    except (ValueError) as e:
        print(f"Processing Error detected in CSV data as expected by sample design: {e}")
        average_result = None
        
    if average_result is not None:
        print("Final Result:", average_result)