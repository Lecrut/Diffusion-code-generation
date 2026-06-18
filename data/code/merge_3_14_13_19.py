import os

def read_volume_measurements(filename: str) -> list[float]:
    """Reads volume measurements from a file, one per line."""
    volumes = []
    
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                stripped_line = line.strip()
                # Skip empty lines if any occur unexpectedly during testing
                if not stripped_line:
                    continue
                
                try:
                    value = float(stripped_line)
                    volumes.append(value)
                except ValueError as e:
                    raise ValueError(f"Invalid volume measurement on line {line_num}: '{stripped_line}'. Error details: {e}") from e
                    
    except IOError as e:
        raise RuntimeError(f"Error reading file '{filename}': {e}") from e
        
    return volumes

def compare_volumes(volume_list: list[float]) -> tuple[int, int]:
    """Compares two volume measurements and returns (index_of_larger, index_of_smaller)."""
    if len(volume_list) != 2:
        raise ValueError("Exactly two volume measurements are required for comparison.")
    
    vol_a = volume_list[0]
    vol_b = volume_list[1]
    
    if vol_a > vol_b:
        return (0, 1)
    elif vol_b > vol_a:
        return (1, 0)
    else:
        # If they are equal, order doesn't strictly matter for 'larger', 
        # but we'll prioritize the first one as larger to maintain consistency.
        return (0, 1)

if __name__ == '__main__':
    # Hard-coded sample values simulating a file read since no pre-existing files are allowed at runtime.
    # In a real scenario with 'volumes.txt', this function would be called externally or the logic adapted to use actual I/O if the file existed.
    # However, per instructions: "The script must handle file I/O errors gracefully" and "sample block must run without ... pre-existing files".
    # We will simulate reading from a non-existent file to demonstrate error handling as requested by the task constraints regarding graceful handling of missing files or invalid states if we strictly follow 'no pre-existing files'.
    
    filename = 'volumes.txt'
    
    try:
        volumes = read_volume_measurements(filename)
        
        # Since no actual file exists in this isolated environment, let's simulate a successful run with hardcoded values 
        # to demonstrate the comparison logic as per "Include an if __name__ == '__main__': block".
        # To make it runnable without files while demonstrating functionality:
        print("Simulating read from 'volumes.txt'...")
        
        sample_v1 = 50.5
        sample_v2 = 75.3
        
        volumes = [sample_v1, sample_v2]
        
    except FileNotFoundError as e:
        # Graceful handling for missing file scenario if we tried to read the real 'volumes.txt'
        print(f"Error: {e}")
        print("Running simulation with hardcoded values instead.")
        volumes = [50.5, 75.3]

    try:
        result_indices = compare_volumes(volumes)
        
        vol_a_idx, vol_b_idx = result_indices
        
        if len(volumes) >= 2:
            val_a = volumes[vol_a_idx]
            val_b = volumes[vol_b_idx]
            
            print(f"Comparison complete.")
            print(f"Larger value ({val_a}) is at index {vol_a_idx}.")
            print(f"Smaller value ({val_b}) is at index {vol_b_idx}.")
        else:
            # Fallback if logic path didn't execute due to empty list (unlikely given simulation)
            pass
            
    except ValueError as e:
        print(f"Comparison error occurred: {e}")