import csv

def read_weights_from_csv(file_path):
    """
    Reads weight measurements from a CSV file grouped by category.
    
    Expects columns named 'category' (string) and 'weight' (float/int).
    Returns a dictionary mapping each unique category to its average weight.
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, float]: Dictionary where keys are categories and values 
                         are the calculated average weights rounded to 2 decimal places.
                         
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If weight data cannot be parsed as numeric or category is missing.
    """
    averages = {}

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Initialize totals and counts for known categories to avoid KeyError on first pass if needed,
            # though a dict initialization is more robust. We will assume 'category' exists per requirement.
            
            for row in reader:
                category = row['category']
                
                try:
                    weight = float(row['weight'])
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid weight value '{row.get('weight')}' found at {csv_file.name}.")

                if category not in averages:
                    # Initialize with 0.0 count and 0.0 sum only after we are sure of the structure
                    averages[category] = {'total': 0, 'count': 0}
                
                current_avg_data = averages[category]
                current_avg_data['total'] += weight
                current_avg_data['count'] += 1
                
            # Final calculation and rounding for performance (avoiding repeated lookups)
        final_averages = {}
        
        for category in averages:
            data = averages[category]
            if data['count'] > 0:
                avg_weight = round(data['total'] / data['count'], 2)
                final_averages[category] = avg_weight
        
        return final_averages

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

if __name__ == '__main__':
    # Hard-coded sample CSV content simulation for robustness testing without interactive input.
    
    class InMemoryCSVReader:
        """A simple helper to simulate an in-memory CSV reader structure."""
        
        def __init__(self, data_rows):
            self.data = data_rows
        
        def read(self):
            return iter(self.data)

        def get_column_names(self):
            # Simulate header row for DictReader expectations if we want full compatibility, 
            # though the sample structure below explicitly uses keys.
            return ['category', 'weight']

    # Define sample data as a list of dictionaries matching CSV format requirements
    sample_data = [
        {'category': 'Adults', 'weight': 70.5},
        {'category': 'Children', 'weight': 35.2},
        {'category': 'Adults', 'weight': 80.1},
        {'category': 'Teenagers', 'weight': 55.0},
        {'category': 'Children', 'weight': 40.5},
    ]

    # Simulate file reading using the in-memory helper and a temporary string path for demonstration
    
    class TempFileSimulator:
        def __init__(self, content):
            self.content = content
        
        @property
        def name(self):
            return "sample_weights.csv"
        
        def open(self, mode='r', encoding='utf-8'):
            import io
            return iter(io.StringIO(self.content))

    # Prepare CSV string content including header and sample data lines
    csv_content = """category,weight
Adults,70.5
Children,35.2
Adults,80.1
Teenagers,55.0
Children,40.5"""