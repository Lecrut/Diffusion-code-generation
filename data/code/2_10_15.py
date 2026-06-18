import re

def parse_volume_file(filename):
    """
    Reads volume measurements from a file, calculates total volume,
    and handles potential float conversion errors gracefully.
    
    Args:
        filename (str): Path to the input file containing volume data.
        
    Returns:
        tuple: (total_volume, error_count) where total_volume is the sum of valid volumes 
               and error_count is the number of lines that failed parsing.
    """
    total_volume = 0.0
    error_count = 0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Strip whitespace and empty lines
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                
                # Attempt to parse the volume from the string
                try:
                    value = float(stripped_line)
                    total_volume += value
                except ValueError as e:
                    error_count += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

def main():
    """
    Main function to run the script with hard-coded sample values.
    Simulates a file input by creating temporary data in memory and processing it directly,
    ensuring no user interaction or external dependencies are required.
    """
    
    # Hard-coded sample volume measurements (simulating file content)
    samples = [10.5, 20.3, "invalid", 30.7, "", -5.2] 
    
    total_volume = sum(samples) if all(isinstance(x, float) for x in samples) else 0.0
    
    # Simulate error handling by manually counting invalid entries
    try:
        valid_sum = 0.0
        error_count = 0
        
        for item in samples:
            stripped_item = str(item).strip() if isinstance(item, (int, float)) else str(item)
            
            try:
                value = float(stripped_item)
                valid_sum += value
            except ValueError:
                error_count += 1
                
    finally:
        print(f"Total Volume Calculated: {valid_sum}")
        if error_count > 0:
            print(f"Gross Error Count (unparseable lines): {error_count}")

if __name__ == '__main__':
    main()