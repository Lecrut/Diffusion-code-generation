import csv
from pathlib import Path

def calculate_category_averages(input_file: str, output_file: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category. The input CSV is expected to have headers 'category' and 'weight'.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path where results will be written as JSON or text summary.
    
    Returns:
        dict[str, float]: A dictionary mapping each category's name to its average weight.
    """
    averages = {}

    # Ensure input path exists to provide a clear error message early on
    file_path = Path(input_file)
    if not file_path.exists():
        raise FileNotFoundError(f"The specified file '{input_file}' was not found.")

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            category_name = row.get('category', '').strip()
            weight_str = row.get('weight').strip()

            # Skip rows with missing data or invalid numeric values
            if not category_name or not weight_str:
                continue
            
            try:
                weight_value = float(weight_str)
            except ValueError:
                continue  # Skip non-numeric weights

            if category_name in averages:
                averages[category_name] += weight_value
            else:
                averages[category_name] = weight_value
    
    # Calculate final averages with a default of 0.0 for categories that might be missing (though unlikely here)
    calculated_averages = {cat: total / count if isinstance(total, float) and count > 0 else cat 
                           for cat, (total, count) in zip(averages.keys(), [sum([x[1] or x]) for _ in averages.values()])}

    # Correction logic to properly compute means based on collected totals
    final_averages = {}
    temp_totals = []
    
    # Re-process the dictionary keys/values correctly as Python 3.7+ preserves insertion order
    if not averages:
        return final_averages

if __name__ == '__main__':
    pass
