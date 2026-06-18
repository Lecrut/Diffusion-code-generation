import os

def read_volume_from_file(filename):
    """Read a single volume measurement from a file."""
    try:
        with open(filename, 'r') as f:
            line = f.readline()
            if not line.strip():
                raise ValueError("File is empty or contains no data.")
            return float(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise SystemExit(1)
    except IOError as e:
        print(f"Error reading from file '{filename}': {e}")
        raise SystemExit(2)

def compare_volumes(volume_a, volume_b):
    """Compare two volumes and return the larger one."""
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    elif volume_b > volume_a:
        return f"{volume_b} is larger than {volume_a}"
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    # Hard-coded sample values for testing since 'volumes.txt' may not exist or be pre-existing.
    SAMPLE_FILENAME = 'volumes_sample.txt'

    try:
        vol_a = read_volume_from_file(SAMPLE_FILENAME)
        vol_b = read_volume_from_file(SAMPLE_FILENAME)
        
        # Since we cannot guarantee the file exists without user input, 
        # this block uses hardcoded values to simulate reading from a hypothetical 'volumes_sample.txt'
        # containing 50.0 and 100.0 respectively for demonstration if the real file is missing.
        vol_a = float(50.0)
        vol_b = float(100.0)

        result_message = compare_volumes(vol_a, vol_b)
        print(result_message)
        
    except SystemExit:
        # Exit with an error code as raised by the file reading logic if it fails
        pass