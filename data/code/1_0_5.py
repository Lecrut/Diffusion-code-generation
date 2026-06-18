import csv

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, list[float]]: A dictionary where keys are categories 
                               and values are lists of float weights.
    """
    weight_data = {}

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            category = row.get('category', '').strip()
            try:
                weight = float(row['weight'].strip())
            except ValueError:
                continue  # Skip rows with invalid numeric values
            
            if category not in weight_data:
                weight_data[category] = []
            
            weight_data[category].append(weight)

    return weight_data

def calculate_average(weights_list):
    """
    Calculates the average value of a list of numbers.
    
    Args:
        weights_list (list[float]): List of numeric values to average.
        
    Returns:
        float or None: The calculated average, or None if the list is empty.
    """
    return sum(weights_list) / len(weights_list)

def process_weight_data(file_path):
    """
    Reads data from a CSV file and calculates the average weight per category.
    
    Args:
        file_path (str): Path to the input CSV file containing 'category' and 
                         'weight' columns.
        
    Returns:
        dict[str, float]: A dictionary mapping each category name to its 
                          corresponding average weight.
    """
    weights_data = read_weights_from_csv(file_path)
    
    averages = {}
    for category in sorted(weights_data.keys()):
        avg_weight = calculate_average(weights_data[category])
        if avg_weight is not None:
            averages[category] = round(avg_weight, 2)

    return averages

if __name__ == '__main__':
    # Hard-coded sample data to simulate reading from a CSV file.
    # The format matches what the function expects (dictionary with 'category' and 'weight').
    
    csv_content = """category,weight
Adults,70.5
Children,32.1
Seniors,68.9
Adults,75.2
Children,40.3
"""

    # Define a temporary file path for the sample data processing logic to work as if reading from disk
    sample_file_path = 'sample_weights.csv'

    with open(sample_file_path, 'w', encoding='utf-8') as f:
        f.write(csv_content)

    averages = process_weight_data(sample_file_path)

    # Output the results directly for verification purposes. 
    print("Average weights per category:")
    for cat in sorted(averages.keys()):
        print(f"{cat}: {averages[cat]}")