import csv

def calculate_average_weight(file_path):
    """
    Reads weight measurements from a CSV file and calculates the average 
    weight for each category defined in the first row headers (except 'weight').
    
    Assumes:
        - The CSV has at least one data row.
        - Headers include 'category' and 'weight'.
        - Data is numeric where needed.

    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict: A dictionary mapping each category name to its average weight.
    """
    averages = {}
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if 'category' not in row or 'weight' not in row:
                    continue
                
                category = row['category'].strip()
                
                # Ensure weight is a valid float before processing to avoid runtime errors on bad data
                try:
                    weight = float(row['weight'])
                except ValueError:
                    print(f"Warning: Skipping invalid weight value '{row.get('weight', '')}' for category '{category}'.")
                    continue
                
                if category not in averages:
                    weights_in_category = []
                    averages[category] = weights_in_category
                
                averages[category].append(weight)

        # Calculate and store the average
        final_averages = {}
        for category, weight_list in averages.items():
            total_weight = sum(weight_list)
            count = len(weight_list)
            
            if count > 0:
                avg_weight = round(total_weight / count, 2)
                final_averages[category] = avg_weight
        
        return final_averages

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while processing the CSV: {e}")
    
    # Return empty dict if an exception happened or no data processed successfully to satisfy return type requirement
    return {}

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes. 
    # Creates a temporary file in memory simulation by writing to a local path, 
    # but since we cannot guarantee write permissions on all environments without tempfile module usage explicitly requested,
    # this block simulates the logic using hardcoded data loaded into a list structure that mimics CSV reading directly 
    # within the function call scope for robustness demonstration.

    sample_data = """category,weight
Apples,150
Bananas,200
Apples,175
Oranges,300
Bananas,225
"""

    import tempfile
    import os
    
    # Write sample data to a temporary file for realistic testing of the main function logic
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
        tmp_name = tmp_file.name
        
        writer = csv.writer(tmp_file)
        writer.writerows(sample_data.strip().split('\n'))

    # Run the calculation on the temporary file
    results = calculate_average_weight(tmp_name)
    
    print("Average weights per category:")
    for cat, avg in sorted(results.items()):
        print(f"{cat}: {avg}")
    
    # Clean up temporary file after execution is complete to prevent disk residue
    os.unlink(tmp_name)