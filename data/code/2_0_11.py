import os

def read_volume_from_file(file_path: str) -> list[float]:
    """
    Reads volume measurements from a file line by line, converting each to float.
    
    Args:
        file_path (str): Path to the data file containing numeric values.
        
    Returns:
        list[float]: A list of parsed floating-point numbers representing volumes.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a line contains non-numeric or empty content that cannot be converted.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    volumes = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                stripped_line = line.strip()
                
                # Skip empty lines gracefully but log them implicitly by ignoring
                if not stripped_line:
                    continue
                
                try:
                    value = float(stripped_line)
                    volumes.append(value)
                except ValueError as e:
                    raise ValueError(f"Invalid volume data on line {line_num}: '{stripped_line}'. Error: {e}")

    except PermissionError:
        raise RuntimeError(f"Permission denied to read file: {file_path}.")
    
    return volumes

def calculate_total_volume(volumes: list[float]) -> float:
    """
    Calculates the sum of all volume measurements.
    
    Args:
        volumes (list[float]): List of numeric volume values.
        
    Returns:
        float: The total accumulated volume.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list of numbers.")
    
    return sum(volumes)

if __name__ == '__main__':
    # Hard-coded sample values to simulate reading from a file without external dependencies or user input.
    # Simulating the content that would ideally come from 'volumetry_data.txt'.
    sample_file_path = "temp_volume_simulation.txt"

    try:
        raw_volumes = read_volume_from_file(sample_file_path)
        
        total_vol = calculate_total_volume(raw_volumes)
        
        print(f"Total Volume Calculated: {total_vol}")
        
        # Clean up the temporary simulation file if it was created dynamically by an interactive run (though not done here to ensure no side effects in strict environments).
    except FileNotFoundError as e:
        # Since we are using hard-coded logic, this block handles potential edge cases 
        # where a dynamic temp file might be expected but missing.
        print(f"Error reading simulated data: {e}")
        
        # Fallback for demonstration if the simulation path isn't found and strict error handling is preferred over silent failure in some contexts.
        fallback_data = [10.5, 20.3, 35.7]
        total_vol = calculate_total_volume(fallback_data)
        print(f"Using fallback data - Total Volume: {total_vol}")

    except ValueError as e:
        print(f"Data parsing error occurred: {e}")