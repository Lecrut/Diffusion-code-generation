import os

def read_volume_from_file(filename):
    """Reads a single volume measurement from the specified file."""
    try:
        with open(filename, 'r') as f:
            line = f.readline().strip()
            if not line:
                return None
            return float(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise SystemExit(1)
    except ValueError:
        print(f"Error: Invalid value in file '{filename}'.")
        raise SystemExit(1)

def compare_volumes(vol_a, vol_b):
    """Compares two volume measurements and returns the larger one."""
    if vol_a is None or vol_b is None:
        return "Invalid input", 0

    if vol_a > vol_b:
        return f"{vol_a} is larger than {vol_b}", int(vol_a) - int(vol_b)
    elif vol_b > vol_a:
        return f"{vol_b} is larger than {vol_a}", int(vol_b) - int(vol_a)
    else:
        return "Both volumes are equal", 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate reading from 'volumes.txt' without requiring the file.
    # In a real scenario, you would call read_volume_from_file('volumes.txt').
    
    vol_a = 50.5
    vol_b = 73.2
    
    result_message, difference = compare_volumes(vol_a, vol_b)
    print(result_message)