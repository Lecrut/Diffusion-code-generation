import csv

def calculate_average_weight(file_path: str) -> dict[str, float]:
    """
    Reads weight measurements from a CSV file and calculates the average weight 
    for each category defined in the 'category' column.

    The expected CSV format is assumed to have two columns: 'weight' (numeric) 
    and 'category' (string). The script will automatically detect headers on the 
    first row. If fewer than 2 rows exist, it may fail gracefully during reading.
    
    Parameters:
        file_path: Path or string of valid CSV file

    Returns:
        Dictionary mapping each category name to its average weight rounded to two decimal places.
        
    Raises:
        FileNotFoundError if the specified path does not point to an existing file.
        ValueError if 'weight' column cannot be parsed as float for any row.
    """

    averages = {}
    
    # Open CSV with UTF-8 encoding and use csv.DictReader for automatic header detection

if __name__ == '__main__':
    pass
