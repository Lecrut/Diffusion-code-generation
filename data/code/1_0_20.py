import csv
from collections import defaultdict

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict: A dictionary where keys are categories and values are lists of weights.
              If no data is found, returns an empty list for each key encountered.
    """
    category_weights = defaultdict(list)

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Check if the CSV has headers and expected columns ('category' and 'weight')
            if not all(col in reader.fieldnames for col in ['category', 'weight']):
                raise ValueError("CSV must contain 'category' and 'weight' columns.")

            for row in reader:
                category = row['category'].strip()
                try:
                    weight = float(row['weight'])
                except ValueError as e:
                    print(f"Warning: Invalid weight value '{row['weight']}' for category {category}. Skipping.")
                    continue
                
                if not isinstance(category, str) or not 0 <= weight < float('inf'):
                    raise ValueError("Invalid data format detected.")

                category_weights[category].append(weight)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

    return dict(category_weights)

def calculate_average(weights_list):
    """
    Calculates the average weight from a list of measurements.
    
    Args:
        weights_list (list[float]): List of numerical weights.
        
    Returns:
        float or None: The calculated average, or None if the list is empty.
    """
    return sum(weights_list) / len(weights_list) if weights_list else 0.0

def main():
    # Hard-coded sample data for demonstration purposes without interactive input
    sample_csv_content = "category,weight\nAdult,75.5\nChild,32.1\nSenior,68.9\nAdult,80.2\nChild,34.5"

    import io
    
    csv_file_obj = io.StringIO(sample_csv_content)
    
    # Simulate reading from a file using the StringIO object as if it were an actual file path
    try:
        with open('sample_data.csv', mode='w', newline='', encoding='utf-8') as temp_file:
            writer = csv.writer(temp_file)
            for line in sample_csv_content.strip().split('\n'):
                writer.writerow(line.split(','))

        # Now read from the created temporary file structure (simulated via actual file write then re-read logic below)
        with open('sample_data.csv', mode='r', newline='', encoding='utf-8') as temp_file:
            reader = csv.DictReader(temp_file)
            
            category_weights = defaultdict(list)

            for row in reader:
                try:
                    weight = float(row['weight'])
                    if isinstance(row.get('category'), str):
                        category_weights[row['category']].append(weight)
                except ValueError:
                    continue
            
            # Calculate averages per category
            results = {}
            for cat, weights in category_weights.items():
                avg_weight = calculate_average(weights)
                results[cat] = round(avg_weight, 2)

            print("Average Weights by Category:")
            for cat, avg in sorted(results.items()):
                print(f"{cat}: {avg} kg")
                
    except Exception as e:
        # Fallback if file creation fails due to permissions or path issues during execution context
        print(f"Error processing sample data directly: {e}")

if __name__ == '__main__':
    main()