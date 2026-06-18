import csv
from collections import defaultdict

def calculate_average_weight(file_path):
    """
    Reads weight measurements from a CSV file and calculates the average 
    weight for each category. Assumes the first row contains headers with 
    'category' and 'weight'. Returns a dictionary mapping categories to their averages.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        dict: A dictionary where keys are category names and values are average weights.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If required columns ('category', 'weight') are missing or data is invalid.
    """
    averages = defaultdict(list)

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Validate headers
            if not any(header in reader.fieldnames for header in ['category', 'weight']):
                raise ValueError("CSV must contain 'category' and 'weight' columns.")

            for row_num, row in enumerate(reader, start=2):  # Start at 2 to account for header row
                category = row.get('category')
                weight_str = row.get('weight', '').strip()

                if not category or not weight_str:
                    continue  # Skip rows with missing data

                try:
                    weight = float(weight_str)
                except ValueError:
                    raise ValueError(f"Invalid weight value '{weight_str}' at line {row_num}.")

                averages[category].append(weight)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    # Calculate and round averages to 2 decimal places for cleaner output
    result = {}
    for category, weights in averages.items():
        if len(weights) > 0:
            avg_weight = sum(weights) / len(weights)
            result[category] = round(avg_weight, 2)

    return result

if __name__ == '__main__':
    # Hard-coded sample data for testing purposes. 
    # In a real scenario, replace 'sample_data.csv' with an actual file path.
    
    csv_content = """category,weight
Apples,150.5
Bananas,200.3
Oranges,175.8
Apples,160.2
Bananas,190.4"""

    # Write sample data to a temporary file for demonstration
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        temp_name = temp_file.name
        temp_file.write(csv_content)

    try:
        averages = calculate_average_weight(temp_name)
        
        print("Average weights by category:")
        for cat in sorted(averages.keys()):
            print(f"{cat}: {averages[cat]} kg")
            
    finally:
        # Clean up the temporary file created during testing
        import os