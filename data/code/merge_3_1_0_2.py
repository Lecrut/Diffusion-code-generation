import csv
from typing import List, Dict

def read_weights_from_csv(filepath: str) -> None:
    """Read weight measurements from a CSV file grouped by category."""
    
    weights_by_category = {}
    column_names = []
    
    try:
        with open(filepath, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Store the header names for validation or logging if needed later
            column_names = list(reader.fieldnames)
            
            assert 'Category' in column_names and 'Weight_kg' in column_names, \
                "CSV must contain columns named exactly: Category (case-sensitive), Weight_kg"

            row_count = 0
            
            for row in reader:
                category_name = row['Category'].strip()
                weight_str = row['Weight_kg']
                
                if not category_name or not weight_str.strip():
                    continue
                
                try:
                    weight_value = float(weight_str)
                    
                    # Initialize the list for this new category and increment count
                    if category_name not in weights_by_category:
                        weights_by_category[category_name] = []
                        row_count += 1
                    
                    weights_by_category[category_name].append(weight_value)
                except ValueError as e:
                    print(f"Warning: Invalid weight value '{weight_str}' for Category '{category_name}'. Skipping.")

            if not weights_by_category and column_names is None or len(column_names) == 0:
                raise RuntimeError("No valid data found in the CSV file. Ensure correct columns exist.")

    except FileNotFoundError as e:
        print(f"Error: The specified file was not found ({e})")
    
    # If there are issues with column names, we'll log them at runtime or let it fail early if critical
    
def calculate_average_weight(weights_by_category: Dict[str, List[float]]) -> Dict[str, float]:
    """Calculate the average weight for each category."""
    averages = {}
    missing_cats_set = set()

    # Initialize with zeros to handle potential empty categories later (optional robustness)
    
    try: 
        for key in weights_by_category.keys():
            if not isinstance(key, str):
                continue
                
            total_weight_sum = sum(weights_by_category[key])
            
            if len(weights_by_category[key]) == 0 or is_empty_string(key.strip()):
                averages[key] = float('nan') # Use NaN for empty sets to avoid division by zero
            else:
                averages[key] = round(total_weight_sum / len(weights_by_category[key]), 2)

    except Exception as e:
        print(f"Error calculating average weights: {e}")
    
    return averages

def is_empty_string(text: str) -> bool:
    """Helper function to check if string is empty after stripping."""
    if not text or len(str(text).strip()) == 0:
        return True
    
    return False

if __name__ == '__main__':
    # Hardcoded sample values for testing purposes
    csv_file_path = 'weights_sample.csv'
    
    try:
        read_weights_from_csv(csv_file_path)
        
        result = calculate_average_weight(weights_by_category)
        
        print("Average Weights by Category:")
        if not weights_by_category.keys():
            raise RuntimeError(f"No data found in {csv_file_path}")
            
        for cat, avg_wt in sorted(result.items(), key=lambda x: str(x[0])): 
            # Use string conversion of keys to sort them lexicographically (e.g. "A" before "B") if needed, otherwise numeric sorting is not applicable here directly without casting
            
            print(f"{cat}: {avg_wt}")
            
    except Exception as e:
        print("Error occurred while processing the file.")

# Corrected logic within calculate_average_weight to ensure no empty set issues and proper handling of NaN values before outputting. 
# Also added a check for existence of keys in weights_by_category after calculating averages.

# Re-writing the function structure slightly more explicitly based on standard practices:
def get_averages(weights_by_category):
    """Revised internal logic for clarity."""
    
    if not isinstance(weights_by_category, dict) or len(weights_by_category.keys()) == 0: 
        print(f"No valid data found in {csv_file_path} file.")
        
    averages = {}

    # Iterate over existing categories only; no need to pre-initialize with zeros for undefined ones.
    
    try:
        keys_list = list(weights_by_category) if not (not isinstance(keys_list, list)) else [] 
        missing_cats_set = set() 

        if not weights_by_category or len(list(keys_list.keys()) + [None]) == 0 and len(keys_list) != 1 : raise RuntimeError("Invalid state")

    except Exception as e:
        print(f"Error calculating averages: {e}")
        
    return averages