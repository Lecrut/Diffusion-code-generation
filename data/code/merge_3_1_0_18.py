import csv

def calculate_category_averages(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category. The expected CSV format is assumed to have columns named 'category' and 'weight'.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, float]: A dictionary mapping each category name to its calculated average weight.
    """
    averages = {}
    total_weight = 0.0
    
    # Open the file with context manager for efficient and safe handling
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                category = row['category'].strip()
                weight_str = row['weight'].strip()
                
                # Convert string to float. If conversion fails, skip the record silently 
                # or handle appropriately depending on robustness requirements. 
                # Here we assume valid numeric input based on task description of 'robust' script logic for expected data.
                try:
                    weight = float(weight_str)
                except ValueError:
                    continue
                
                if category not in averages:
                    total_weight_for_cat = 0.0
                    count_for_cat = 0
                    
                    # Initialize a helper structure to track sums and counts per category 
                    # This inline logic ensures we don't need an extra data structure for the sum/count tracking
                    # We will accumulate here directly into 'averages' dict by storing (sum, count) tuples initially?
                    # Actually, let's restructure slightly: use a dictionary of lists or just two dicts.
                    # To be truly efficient and clean without intermediate structures if possible in one pass:
                    
                    # Re-evaluating approach for single pass efficiency:
                    # We can store (sum_of_weights, count) directly in the averages dict under each category key
                    
                else:
                    total_weight += weight
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return {}

# Revised efficient implementation inside the function to avoid double storage logic above
def calculate_category_averages_v2(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category. The expected CSV format is assumed to have columns named 'category' and 'weight'.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, float]: A dictionary mapping each category name to its calculated average weight.
    """
    # Dictionary where keys are categories and values are tuples of (total_weight, count)
    category_stats = {}
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                category = row['category'].strip() if isinstance(row.get('category'), str) else ''
                weight_str = row['weight'].strip() if isinstance(row.get('weight'), str) else '0'
                
                try:
                    weight = float(weight_str)
                except ValueError:
                    continue
                
                # Initialize category stats if not present, otherwise update sum and count
                if category in category_stats:
                    current_sum, current_count = category_stats[category]
                    new_sum = current_sum + weight
                    new_count = current_count + 1
                    category_stats[category] = (new_sum, new_count)
                else:
                    category_stats[category] = (weight, 1)
                    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    
    # Calculate averages from accumulated stats
    result_averages = {cat: sum_val / count for cat, (sum_val, count) in category_stats.items() if count > 0}
    return result_averages

if __name__ == '__main__':
    sample_data_content = """category,weight
Adult,75.5
Child,32.1
Senior,68.9
Adult,80.2
Child,29.4"""

    # Create a temporary CSV file with the hardcoded sample values to simulate reading from disk
    import tempfile
    
    temp_file = None