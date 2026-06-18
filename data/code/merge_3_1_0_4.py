import csv
from collections import defaultdict

def read_weight_measurements(file_path):
    """
    Reads weight measurements from a CSV file and organizes them by category.
    
    Expected CSV format: 'category,weight' (header required)
    
    Args:
        file_path (str): Path to the input CSV file.
        
    Returns:
        dict[str, list[float]]: Dictionary where keys are categories 
                                and values are lists of weight measurements.
                            
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a category is missing in expected column 'category'.
    
    """
    weights_by_category = defaultdict(list)

if __name__ == '__main__':
    pass
