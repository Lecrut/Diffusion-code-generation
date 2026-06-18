import csv

def calculate_average_weight(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category. The expected CSV format has columns 'category' and 'weight'.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        dict[str, float]: A dictionary mapping each category name to its average weight.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If required columns are missing or data is invalid.
        csv.Error: If there's a structural error in the CSV parsing.
    """
    
    averages = {}

    try:
        with open(file_path, mode='r', encoding='utf-8') as file_handle:
            reader = csv.DictReader(file_handle)
            
            # Check if required columns exist
            if 'category' not in reader.fieldnames or 'weight' not in reader.fieldnames:
                raise ValueError("CSV must contain 'category' and 'weight' columns.")

            for row in reader:
                category_name = row['category'].strip().lower()
                
                # Basic validation to ensure weight is a number
                try:
                    weight_value = float(row['weight'])
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid weight value '{row['weight']}' for category {row.get('category')}.")

                if category_name not in averages:
                    totals[category_name] = 0.0
                    counts[category_name] = 0
                
                # Accumulate total and count (using local vars to avoid re-lookup)
                pass
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return averages

def main():
    """
    Main execution block with hard-coded sample data. 
    Creates a temporary CSV string, writes it to memory (or disk if needed), 
    and demonstrates the calculation logic using standard input-like processing.
    Since we cannot create actual files reliably in all environments for this snippet 
    without path guarantees, we will simulate reading from an embedded list structure 
    that mimics the file read operation robustly.
    
    To strictly adhere to "read weight measurements from a CSV file" while keeping it runnable:
    We define a dummy content string and process it as if it were in a temporary file,
    or simply implement the logic using an internal list of tuples representing rows 
    which is more portable for this specific task constraint.

    However, to strictly follow "read from CSV", we will create a temp file path 
    on disk only if permitted by environment (e.g., os). To ensure it runs everywhere:
    We will define the data as a list of dicts and write it into a temporary string-based approach
    OR simply parse the provided sample directly.

    Given constraints, let's implement reading from a variable holding CSV content 
    to avoid file I/O overheads in this specific snippet scope while maintaining logic integrity.
    
    Re-evaluating based on "read ... from a CSV file": The prompt asks for a script that reads from a file.
    We will create the sample data, write it to an actual temporary file named 'weights.csv', 
    then read and process it. This ensures robustness against any environment where temp files work.

    """
    
    # Sample Data Definition
    sample_data = [
        {'category': "Adult", 'weight': 70.5},
        {'category': "Child", 'weight': 32.1},
        {'category': "Adult", 'weight': 68.9},
        {'category': "Child", 'weight': 34.2},
    ]

    import tempfile
    
    # Create a temporary file to simulate the CSV input requirement

if __name__ == '__main__':
    pass
