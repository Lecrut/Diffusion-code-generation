import csv
from collections import defaultdict

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, list[float]]: A dictionary mapping each category name 
                                to a list of its corresponding weights.
                                
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If required columns ('category', 'weight') are missing or invalid.
    """
    categories = defaultdict(list)

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Validate headers exist and contain required columns (case-insensitive check for robustness)
            if not any(col.lower() in ['category'] for col in reader.fieldnames):
                raise ValueError("CSV file must have a 'Category' column.")
            if not any(col.lower() in ['weight'] for col in reader.fieldnames):
                raise ValueError("CSV file must have a 'Weight' column.")

            # Ensure the header is actually present (handle empty files)
            if len(reader.fieldnames) == 0:
                return categories
                
            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming row 1 is header
                category = None
                weight_str = None

                # Find column indices dynamically to handle case variations or extra spaces
                col_names_lower = [name.lower().strip() for name in reader.fieldnames]
                
                if 'category' in col_names_lower:
                    idx_cat = col_names_lower.index('category')
                    category = row.get(idx_cat, '').strip()
                    
                    # Skip rows with empty categories to avoid errors later
                    if not category or category == "":
                        continue
                        
                else:
                    raise ValueError("Column 'Category' is missing.")

                if 'weight' in col_names_lower:
                    idx_wt = col_names_lower.index('weight')
                    weight_str = row.get(idx_wt, '').strip()
                    
                    # Skip rows with empty weights or non-numeric values
                    try:
                        float(weight_str)
                    except ValueError:
                        continue
                        
                else:
                    raise ValueError("Column 'Weight' is missing.")

                if category and weight_str:
                    categories[category].append(float(weight_str))
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    return dict(categories)

def calculate_average(weights_list):
    """
    Calculates the average of a list of numbers.
    
    Args:
        weights_list (list[float]): List of weight values.
        
    Returns:
        float or None: The calculated average, or None if the list is empty.
    """
    if not weights_list:
        return None
    
    total = sum(weights_list)
    return round(total / len(weights_list), 2)

def main():
    # Hard-coded sample values for testing without interactive input
    sample_csv_content = "Category,Weight\nChild,30.5\nAdult,75.0\nSenior,68.2\nChild,45.1\n"

    # Create a temporary file path and write the content to simulate reading from disk
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
        tmp_path = tmp_file.name
        print(f"Writing sample data to {tmp_path}...")
        
        # Write header and rows manually since we are simulating the file content
        lines = ["Category,Weight", "Child,30.5", "Adult,75.0", "Senior,68.2", "Child,45.1"]
        tmp_file.write('\n'.join(lines) + '\n')

    try:
        # Read the data from our temporary file
        print("Reading weights...")
        weight_data = read_weights_from_csv(tmp_path)
        
        if not weight_data:
            print("No valid weight categories found.")
            return
            
        print("\nCategory Averages:")
        all_averages_ok = True
        
        for category, weights in sorted(weight_data.items()):
            avg_weight = calculate_average(weights)
            
            # Check for division by zero or empty list edge cases (though handled internally)
            if isinstance(avg_weight, float):
                print(f"{category}: {avg_weight} kg")
                
    finally:
        # Clean up the temporary file created during testing
        import os
        try:
            os.unlink(tmp_path)
        except OSError:
            pass

if __name__ == '__main__':
    main()