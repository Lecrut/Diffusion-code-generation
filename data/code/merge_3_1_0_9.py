import csv
from collections import defaultdict

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict: A dictionary where keys are categories and values are lists of weights.
    """
    if not isinstance(file_path, str) or not file_path.endswith('.csv'):
        raise ValueError("File path must be a string ending with '.csv'")

    weight_data = defaultdict(list)

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Validate required columns exist in the first row
            if not reader.fieldnames or 'category' not in reader.fieldnames or 'weight' not in reader.fieldnames:
                raise ValueError("CSV file must contain 'category' and 'weight' columns")

            for index, row in enumerate(reader):
                category = row.get('category')
                weight_str = row.get('weight', '').strip()

                if not category or not weight_str:
                    continue  # Skip rows with missing data

                try:
                    weight = float(weight_str)
                    if weight < 0:
                        raise ValueError(f"Weight cannot be negative at index {index}")
                    
                    weight_data[category].append(weight)
                except (ValueError, TypeError):
                    continue  # Skip rows with invalid numeric data

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the file '{file_path}'.")
    
    return dict(weight_data)

def calculate_average_weight(data):
    """
    Calculates the average weight for each category.

    Args:
        data (dict): Dictionary of categories and their respective weights lists.

    Returns:
        dict: A dictionary where keys are categories and values are average weights rounded to 2 decimal places.
        
    Raises:
        ValueError: If a category has no valid weight entries.
    """
    averages = {}
    
    for category, weights in data.items():
        if not weights or len(weights) == 0:
            raise ValueError(f"No valid weight measurements found for category '{category}'.")

        average_weight = sum(weights) / len(weights)
        averages[category] = round(average_weight, 2)
    
    return averages

if __name__ == '__main__':
    # Hard-coded sample data simulation to demonstrate functionality without interactive input
    import tempfile
    import os
    
    temp_file_path = None

    try:
        # Create a temporary CSV file with sample data for testing
        csv_content = """category,weight
Apples,1.5
Bananas,0.8
Oranges,2.3
Apples,1.7
Bananas,0.9
Milk,2.5
Milk,2.6
Water,3.0
"""

        temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        temp_file_path.write(csv_content)
        temp_file_path.close()

        # Read data from the temporary file
        weight_data = read_weights_from_csv(temp_file_path.name)

        if not weight_data:
            print("No valid data found.")
        else:
            averages = calculate_average_weight(weight_data)
            
            for category, avg in sorted(averages.items()):
                print(f"{category}: {avg} kg")
    finally:
        # Clean up the temporary file to ensure no resource leaks on exit
        if temp_file_path and os.path.exists(temp_file_path.name):
            try:
                os.remove(temp_file_path.name)
            except OSError as e:
                print(f"Warning: Could not remove temporary file: {e}")