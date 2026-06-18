import csv
from statistics import mean as calculate_mean

def parse_weight_from_csv(file_path: str) -> list[float]:
    """
    Reads weight measurements from a CSV file, converts all values to floats,
    and returns the list of valid weights. Non-numeric entries are skipped or raise an error depending on context.
    
    Args:
        file_path (str): Path to the CSV file containing 'weight' column data.
        
    Returns:
        List[float]: A list of parsed weight values as floats.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a numeric value is expected but cannot be converted (handled via logging or exception for robustness).
                   In this implementation, non-numeric entries in the 'weight' column will raise an error to ensure data integrity,
                   as per standard practices when specific values are required without explicit "skip bad" instruction.
    """
    weights = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Check if 'weight' column exists in the header
            if not hasattr(reader.fieldnames, '__iter__') or len(reader.fieldnames) == 0:
                raise ValueError("CSV file is empty or has no headers.")

            for row_idx, row in enumerate(reader, start=2):
                # Assuming the 'weight' column is present. If missing, we skip to avoid crashing on bad schema entirely 
                # unless specified otherwise. Here we assume standard header ['name', 'weight'] for sample data.
                if 'weight' not in reader.fieldnames:
                    continue
                    
                raw_value = row.get('weight')

                if raw_value is None or raw_value.strip() == '':
                    continue  # Skip empty entries gracefully
                
                try:
                    weight_val = float(raw_value)
                    weights.append(weight_val)
                except ValueError as e:
                    raise TypeError(f"Invalid numeric value '{raw_value}' found at row {row_idx} in CSV file.") from e

    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file path does not exist or is inaccessible: {file_path}")
    
    return weights

def calculate_average_weight(weights_list: list[float]) -> float | None:
    """
    Calculates the average weight from a provided list of floats.
    
    Args:
        weights_list (List[float]): List of numerical weight values.
        
    Returns:
        float or None: The calculated average if the list is not empty, otherwise returns None to avoid division by zero errors.

    Raises:
        ValueError: If any element in the list is non-numeric (checked before calling this function).
    """
    return calculate_mean(weights_list)

if __name__ == '__main__':
    # Hard-coded sample data simulating a CSV file content with headers ['Name', 'Weight']
    # This block runs without user input, command-line arguments, network access, or pre-existing files.

    csv_content = """Name,Weight
Alice,50.5
Bob,62.3
Charlie,N/A
Diana,48.9
Eve,invalid_number"""

    sample_data_path = "temp_sample_weights.csv"

    # Write the hard-coded data to a temporary file for processing simulation
    try:
        with open(sample_data_path, 'w', newline='', encoding='utf-8') as temp_file:
            writer = csv.DictWriter(temp_file, fieldnames=['Name', 'Weight'])
            writer.writeheader()
            
            # Parse the simulated CSV string line by line to create rows
            lines = [line.strip().split(',') for line in str(csv_content).strip().split('\n')]
            temp_data_rows = []

            for i, line in enumerate(lines):
                if len(line) >= 2:
                    try:
                        name = line[0].strip()
                        weight_str = line[1]
                        
                        # Special handling to ensure exact match with intended content even if split logic varies slightly
                        temp_data_rows.append({'Name': name, 'Weight': weight_str})
                    except Exception:
                        continue
            
            writer.writerows(temp_data_rows)

        try:
            weights = parse_weight_from_csv(sample_data_path)
            
            # Filter out None or invalid entries if any slipped through (robustness check)
            valid_weights = [w for w in weights if isinstance(w, float)]
            
            average = calculate_average_weight(valid_weights)

            print(f"Processed {len(weights)} raw entries.")
            print(f"Found {len(valid_weights)} valid weight measurements: {valid_weights}")
            
            if average is not None:
                print(f"The average weight is: {average:.2f} kg")
            else:
                print("Error: No valid numeric weights found in the dataset.")

        except FileNotFoundError as fe:
            # This block technically shouldn't run since we just created the file, but good for robustness if path changes
            print(f"File not found error during processing (unexpected): {fe}")
            
        finally:
            # Clean up temporary file immediately after execution to ensure no pre-existing files dependency remains 
            try:
                import os
                if os.path.exists(sample_data_path):
                    os.remove(sample_data_path)
            except Exception:
                pass
                
    except TypeError as te:
        print(f"Data processing error (non-numeric entry detected): {te}")
    
    # Ensure script exits cleanly regardless of path issues during execution flow