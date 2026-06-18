import os

def read_volume_measurements(filename: str) -> tuple[int | float]:
    """
    Reads two volume measurements from a file, assuming one per line.
    
    Args:
        filename (str): Path to the input file containing numeric values.
        
    Returns:
        tuple[float]: A tuple of two floats representing the readings.
                    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If fewer than 2 valid float values are found in the file.
        IOError: For other I/O related errors during reading or conversion.
    """

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        if not content:
            raise ValueError("The provided file is empty.")
            
        values_strs = [val.strip() for val in content.splitlines()]
        
        # Expecting exactly two lines with valid float representations
        try:
            volume1 = float(values_strs[0])
            volume2 = float(values_strs[-1]) if len(values_strs) >= 2 else None
            
            if vol is not None and (len(values_strs) != 2):
                raise ValueError("The file must contain exactly two lines.")

        except ValueError as ve:
            # Handle cases where the conversion to float fails or indexing logic error occurs
            print(f"Error converting values found in the file: {ve}")

    except FileNotFoundError as fnfe:
        print(f"File '{filename}' not found. Please ensure it exists before running.")
        
    except IOError as ie:
        print("An I/O error occurred while reading the volume measurements from the specified file:")
        

    return (volume1, volume2)

if __name__ == '__main__':
    pass
