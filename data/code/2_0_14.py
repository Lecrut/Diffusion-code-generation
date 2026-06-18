import os

def read_volume_from_file(file_path: str) -> float | None:
    """
    Reads a single volume measurement from the specified file.
    
    Args:
        file_path (str): Path to the text file containing the volume measurement.
        
    Returns:
        float or None: The parsed volume if successful, otherwise returns None.
                       Handles potential errors like missing files, permissions, 
                       and non-numeric content gracefully without raising exceptions.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line = f.readline().strip()
            
            if not line or '.' in line:
                # Attempt to parse the value; handle potential non-numeric strings gracefully
                return float(line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_path}'.")
    except ValueError as ve:
        # If the line is empty or non-numeric, we assume it's invalid data for this simple script.
        pass
    
    return None

def calculate_total_volume(file_paths: list[str]) -> float | None:
    """
    Calculates the total volume from multiple files.
    
    Args:
        file_paths (list): List of strings representing paths to measurement files.
        
    Returns:
        float or None: The sum of all valid volumes found, rounded to 4 decimal places.
                       If no valid data is found across any provided file, returns None.
    """
    total_volume = 0.0
    
    for path in file_paths:
        value = read_volume_from_file(path)
        
        if value is not None and isinstance(value, (int, float)):
            try:
                total_volume += float(str(int(round(float(value), decimals=1)))) # Ensure consistent handling of floats/ints
            except ValueError:
                continue
                
    return round(total_volume, 4)

if __name__ == '__main__':
    # Sample data simulation without user input or file dependencies.
    sample_files = [
        "volume_data_01.txt", 
        "volume_data_02.txt"
    ]

    calculated_total = calculate_total_volume(sample_files)

    if calculated_total is not None:
        print(f"\nTotal Volume Calculated from Sample Files:")
        print(f"{calculated_total}")
    else:
        print("\nCould not calculate total volume due to missing or invalid data in sample files.")