import csv
from collections import defaultdict

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict: A dictionary where keys are categories and values are lists of weights.
              If no data is found, returns an empty list for all keys encountered or {}.
    """
    category_weights = defaultdict(list)

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Check if the CSV has headers and expected columns ('category' and 'weight')
            if not any(col.lower() in ['category', 'name'] for col in reader.fieldnames):
                raise ValueError("CSV must contain a column named 'category'.")

            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming header is on line 1
                category = row.get('category') or row.get('name', '').strip()
                
                if not category:
                    continue
                    
                try:
                    weight_str = row['weight']
                    weight = float(weight_str)
                    
                    if isinstance(category, str):
                        # Ensure the key is a string for dictionary consistency
                        category_weights[category].append(weight)
                        
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipping invalid data at row {row_num}: {e}")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except csv.Error as e:
        raise ValueError(f"CSV parsing error occurred: {e}")

    return category_weights

def calculate_average(weights_list):
    """
    Calculates the average weight from a list of weights.
    
    Args:
        weights_list (list[float]): List of numerical weights.
        
    Returns:
        float or None: The calculated average, or None if the list is empty.
    """
    if not weights_list:
        return None
    
    total = sum(weights_list)
    return round(total / len(weights_list), 2)

def main():
    # Hard-coded sample values for testing without interactive input
    sample_csv_content = """category,weight
Adult,70.5
Child,35.2
Senior,68.9
Adult,71.0
Child,34.8"""

    import io
    
    # Create a temporary file-like object to simulate reading from disk for the test block
    input_stream = io.StringIO(sample_csv_content)
    
    # Simulate file path logic by writing content to a temp string and using it directly 
    # or simply parsing the StringIO as if it were an open file.
    # To strictly adhere to "read weight measurements from a CSV file", we will write 
    # this sample data to a temporary real file on disk for robustness demonstration,
    # then read it back in the logic flow below.

    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        temp_file.write(sample_csv_content)
        temp_path = temp_file.name

    try:
        weights_data = read_weights_from_csv(temp_path)
        
        averages = {}
        for category in sorted(weights_data.keys()):
            weight_list = weights_data[category]
            avg_weight = calculate_average(weight_list)
            if avg_weight is not None:
                averages[category] = f"{avg_weight} kg"

    finally:
        # Clean up the temporary file created during testing
        import os
        try:
            os.unlink(temp_path)
        except OSError:
            pass  # Ignore errors on cleanup in this isolated context

    print("Average weights by category:")
    for cat, avg in averages.items():
        print(f"{cat}: {avg}")

if __name__ == '__main__':
    main()