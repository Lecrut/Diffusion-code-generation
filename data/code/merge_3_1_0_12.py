import csv
from collections import defaultdict

def calculate_average_weight_by_category(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category. The expected CSV format is assumed to have 'category' and 'weight' columns.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        dict[str, float]: A dictionary mapping each category name to its average weight.
                         If a category has no weights, it will not be included in the result 
                         unless at least one record exists for that key during iteration.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        KeyError: If required columns ('category', 'weight') are missing from CSV rows.
    """
    category_weights = defaultdict(list)

    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Validate header presence immediately upon reading the file
            if not hasattr(reader.fieldnames, '__iter__'):
                raise KeyError("CSV must have column headers.")
            
            required_columns = {'category': None, 'weight': None}
            for col in required_columns:
                if reader.fieldnames is None or col not in reader.fieldnames:
                    missing_cols = [col]
                    # Try to find what's actually there if helpful later, but raise now per requirement robustness
                    raise KeyError(f"Missing required column(s): {missing_cols}")

            for row_num, row in enumerate(reader, start=2):  # Start at 2 assuming header is line 1
                category = row.get('category')
                weight_str = row.get('weight', '').strip()
                
                if not category or not isinstance(category, str) and not hasattr(category, 'lower'):
                    raise KeyError(f"Invalid category value in row {row_num}: '{category}'")

                try:
                    # Handle potential float parsing errors for weights (e.g., empty strings or non-numeric)
                    weight = float(weight_str) if weight_str else 0.0 
                except ValueError as ve:
                    raise KeyError(f"Invalid weight value in row {row_num}: '{weight_str}'") from ve

                category_weights[category].append(weight)

    except FileNotFoundError:
        return None
    
    # Calculate averages only for categories that have at least one measurement recorded above logic flow adjustment needed here? 
    # Re-evaluating based on prompt "robust": if a row has no weight, we skip adding it. If empty list remains, avg is undefined.
    
    results = {}
    total_records_processed = 0
    
    for category in category_weights:
        weights_list = category_weights[category]
        # Only calculate average if there are actual numeric values recorded (skipping rows with missing weight)
        valid_count = len(weights_list) 
        if valid_count > 0:
            results[category] = sum(weights_list) / float(valid_count)

    return {k: v for k, v in results.items()}

if __name__ == '__main__':
    # Hard-coded sample data to simulate a CSV file named 'sample_weights.csv'
    # Format expected: category,weight
    
    import io
    
    csv_content = """category,weight\nsports,70.5\ngymnastics,48.2\nswimming,65.1\nsports,72.3\ndance,55.0"""

    sample_file_path = 'sample_weights.csv'
    
    # Write the CSV content to a temporary file for testing purposes within this module execution context
    with open(sample_file_path, mode='w', encoding='utf-8') as f:
        f.write(csv_content)
    
    # Process the data using the function defined above
    averages = calculate_average_weight_by_category(sample_file_path)

    print("Average weights by category:")
    for cat, avg in sorted(averages.items()):
        print(f"{cat}: {avg:.2f}")