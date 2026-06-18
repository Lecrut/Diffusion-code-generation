import csv

def calculate_average_temperature(filepath: str) -> float | None:
    """
    Reads temperature values from a CSV file, filters non-numeric entries,
    calculates the average, and handles I/O errors gracefully.
    
    Args:
        filepath (str): Path to the input CSV file containing temperature data.
        
    Returns:
        float or None: The calculated average temperature if successful, 
                       otherwise returns None upon error handling completion.
    """
    temperatures = []
    
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            # Assume the first row is headers and look for a column named 'temperature' or similar
            reader = csv.DictReader(csvfile)
            
            if not any(key.lower() == 'temperature' for key in (reader.fieldnames or [])):
                return None
            
            target_col_idx = next(i for i, k in enumerate(reader.fieldnames) if k.lower().startswith('temper'))
            
            count = 0
            total_sum = 0.0
            
            try:
                sum_rows = list(csvfile) # Reload content to iterate properly with DictReader logic or restart context
                
                # Re-iterate using the file object again since we consumed it in 'sum_rows' definition above if not careful, 
                # but actually we can just re-read inside a fresh loop within try block for safety.
                
            except Exception:
                return None

        # Reset iteration approach to be strictly single-pass and robust without reloading state issues
        
        temperatures = []
        
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        raise SystemExit(1)
    
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file at '{filepath}'.")
        return None
        
    except csv.Error as e:
        print(f"CSV parsing error occurred for file: {e}")
        return None
        
    except Exception as generic_error:
        # Generic catch-all for unexpected I/O issues like encoding problems on some systems
        print(f"An unexpected error occurred while reading the CSV data: {generic_error}")
        raise SystemExit(1)

if __name__ == '__main__':
    pass
