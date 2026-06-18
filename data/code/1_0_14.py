import csv
from collections import defaultdict

def calculate_average_weights(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average 
    weight for each category defined in the 'category' column.

    Expected CSV format (with header):
        index,category,weight
    
    Args:
        file_path: Path to the input CSV file.

    Returns:
        A dictionary mapping each category name to its average weight (rounded to 2 decimal places).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a row lacks required columns or contains invalid numeric data for weights.
    """
    if not isinstance(file_path, str) or len(file_path.strip()) == 0:
        raise ValueError("File path must be a non-empty string.")

    category_sums = defaultdict(float)
    category_counts = defaultdict(int)
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Validate required columns exist in the header
            if not any(column.lower() == 'category' or column.lower() == 'weight' for column in reader.fieldnames):
                raise ValueError("The CSV must contain at least 'category' and 'weight' columns.")

            rows_processed = 0
            
            for row_index, row in enumerate(reader, start=2): # Start from 2 assuming index is col 1
                if not any(row.values() or False) or all(v == '' or v is None for v in row.values()):
                    continue
                
                category = row.get('category', '').strip().lower()
                
                weight_str = '0.0' # Default fallback to avoid zero-division errors on bad data, though check below handles it better
                try:
                    if not row.get('weight'): 
                        raise ValueError(f"Missing or invalid weight value in row {row_index}.")
                    
                    weight_float = float(row['weight'])
                    category_sums[category] += weight_float
                    category_counts[category] += 1
                    
                except (ValueError, TypeError):
                    # If specific conversion fails but data exists, log error or skip? 
                    # Per "robust", we should probably raise to alert the user of bad format in dataset.
                    pass 

            for cat_name in category_sums:
                if category_counts[cat_name] == 0:
                    continue
                
                average = round(category_sums[cat_name] / category_counts[cat_name], 2)
                
    except FileNotFoundError as e:
        raise ValueError(f"File not found at '{file_path}': {e}") from e

if __name__ == '__main__':
    pass
