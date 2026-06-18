import csv
from statistics import mean as calculate_mean

def parse_weight_column(file_path: str) -> list[float]:
    """
    Reads a CSV file containing weight measurements in the first column,
    converts values to floats, and returns a clean list of weights.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        list[float]: List of parsed floating-point weights.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric entries are encountered in the weight column.
    """
    weights = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Iterate over rows to skip headers if present and extract data
        for row_num, row in enumerate(reader):
            if not row or all(cell.strip() == '' for cell in row):
                continue
                
            weight_str = row[0].strip().lower()

            try:
                weights.append(float(weight_str))
            except ValueError:
                raise ValueError(f"Invalid numeric entry at line {row_num + 1}: '{weight_str}'")

    return weights

def calculate_average_weight(weights: list[float]) -> float | None:
    """
    Calculates the average weight from a provided list.
    
    Args:
        weights (list[float]): List of floating-point weights.
        
    Returns:
        float or None: The calculated average if the list is not empty, 
                       otherwise returns None to indicate insufficient data.
                       
    Raises:
        ValueError: If an unexpected error occurs during calculation logic.
    """
    try:
        return calculate_mean(weights)
    except Exception as e:
        raise ValueError(f"Error calculating average weight: {e}")

if __name__ == '__main__':
    # Hard-coded sample values simulating a CSV file structure with headers and data rows.
    # Format expected by the script: 'weight,value' where value is in column 0 (index).
    
    import io
    
    csv_content = """weight,measurement_id
75.5,id_1
82.3,id_2
69.8,id_3"""

    file_path = "sample_weights.csv"

    try:
        # Write sample data to a temporary file for demonstration purposes within the same process context
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['weight', 'measurement_id'])
            
            weights_data = [75.5, 82.3, 69.8]
            for w in weights_data:
                writer.writerow([f"{w}", "id_" + str(len(weights_data))])

        # Read and process the file created above
        raw_weights = parse_weight_column(file_path)
        
        if not raw_weights:
            print("No valid weight data found.")
        else:
            average_wt = calculate_average_weight(raw_weights)
            
            if average_wt is None:
                print("Could not compute average due to empty dataset.")
            else:
                print(f"Average Weight: {average_wt:.2f} kg")

    except FileNotFoundError as e:
        # This block handles the case where no file exists, though we just created one above.
        # It serves robustness for actual usage scenarios.
        print(f"Error: File not found - {e}")
        
    except ValueError as ve:
        # Handles non-numeric entries or calculation errors
        print(f"Data Error encountered:\n{ve}")

    finally:
        # Clean up the temporary file created during this session execution to maintain cleanliness.
        import os
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as cleanup_err:
                print(f"Warning while cleaning up temp file: {cleanup_err}")