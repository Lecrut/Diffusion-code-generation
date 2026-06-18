import csv
from statistics import mean as calculate_average

def process_weight_file(filename):
    """
    Reads weight measurements from a CSV file, converts values to floats,
    calculates the average weight with error handling.

    Args:
        filename (str): Path to the input CSV file.
    
    Returns:
        float or None: The calculated average weight if successful, else None.
    """
    weights = []

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            for row_num, row in enumerate(reader):
                # Skip empty rows or malformed lines that don't have enough columns
                if not row or len(row) == 0:
                    continue
                
                try:
                    weight_value = float(row[0])
                    weights.append(weight_value)
                except ValueError:
                    print(f"Warning: Skipping non-numeric entry at line {row_num + 2}: '{row[0]}'")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except csv.Error as e:
        print(f"CSV Error reading file: {e}")
        return None
    
    if len(weights) == 0:
        return None

    average_weight = calculate_average(weights)
    return average_weight

if __name__ == '__main__':
    # Hard-coded sample data for testing without external files or user input.
    
    csv_data_str = """weight,measurement_type,date
75.2,kilograms,2023-10-01
68.5,pounds,2023-10-05
invalid_entry,kilograms,2023-10-10
79.8,kilograms,2023-10-15"""

    # Create a temporary file path for the sample data logic (simulating reading from disk)
    temp_filename = "sample_weights.csv"
    
    try:
        # Write the hardcoded CSV string to a temporary file first 
        # so the main function can read it as if loading an external resource.
        with open(temp_filename, 'w', encoding='utf-8') as f:
            f.write(csv_data_str)

        result = process_weight_file(temp_filename)
        
        print(f"Calculated Average Weight: {result}")
    finally:
        # Cleanup temporary file to keep the environment clean for subsequent runs.
        try:
            import os
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
        except Exception:
            pass  # Ignore cleanup errors as they are non-critical in this isolated context.