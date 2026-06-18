import os

def read_volume_file(filepath: str) -> list[float]:
    """
    Reads volume measurements from a file containing one value per line.
    
    Args:
        filepath (str): Path to the input file.
        
    Returns:
        list[float]: A list of parsed float values found in the file.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a non-numeric value is encountered during parsing.
    """
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file {filepath} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the file {filepath}.")
    
    volumes = []
    
    for idx, line in enumerate(lines):
        # Strip whitespace and ignore empty lines silently or skip them
        stripped_line = line.strip()
        
        if not stripped_line:
            continue
            
        try:
            value = float(stripped_line)
        except ValueError as e:
            raise ValueError(f"Invalid numeric data on line {idx + 1}: '{stripped_line}'") from e
        
        volumes.append(value)
    
    return volumes

def calculate_total_volume(volumes: list[float]) -> float:
    """
    Calculates the total volume sum of a given list.
    
    Args:
        volumes (list[float]): List of individual measurements.
        
    Returns:
        float: The sum of all elements in the list.
    """
    return sum(volumes)

if __name__ == '__main__':
    # Hard-coded sample data simulating a file named 'volumemeasurements.txt'
    # containing two volume measurements for demonstration purposes.
    
    SAMPLE_FILE_PATH = "sample_data.txt"
    
    try:
        raw_volumes = read_volume_file(SAMPLE_FILE_PATH)
        
        if not raw_volumes:
            print("No valid volume data found.")
        else:
            total_volume = calculate_total_volume(raw_volumes)
            
            # Print results in a clean format, e.g., "Total Volume (L): 5.0"
            formatted_output = f"Total Volume ({len(raw_volumes)} measurements): {total_volume:.2f}"
            print(formatted_output)
            
    except FileNotFoundError as fe:
        # Graceful handling for the case where sample_data.txt does not exist locally
        print(f"Error: Could not find required file '{SAMPLE_FILE_PATH}'. " +
              f"In this environment, please ensure it exists or modify the script to run directly.")
        
    except ValueError as ve:
        print("Data Error:", str(ve))