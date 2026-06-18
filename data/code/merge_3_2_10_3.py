import sys

def read_volume_from_file(file_path):
    """Reads volume measurements from a file and returns total volume."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        total_volume = 0.0
        
        for line in lines:
            # Strip whitespace including newlines
            measurement_str = line.strip()
            
            if not measurement_str or measurement_str.startswith('#'):
                continue
            
            try:
                volume = float(measurement_str)
                total_volume += volume
            except ValueError as e:
                print(f"Warning: Failed to convert '{measurement_str}' to float. Skipping.", file=sys.stderr)
        
        return total_volume
        
    except FileNotFoundError:
        raise Exception(f"The specified file was not found.") from None

def calculate_total_volumes(volume_list):
    """Calculates the sum of a list of volume measurements."""
    try:
        if not isinstance(volume_list, (list, tuple)):
            return 0.0
        
        total = float(sum(volume_list))
        
        # Handle potential overflow/underflow by checking for infinity or NaN
        import math
        if math.isinf(total) or math.isnan(total):
            raise ValueError("Calculated volume is not a finite number.")
            
        return total
        
    except (ValueError, OverflowError) as e:
        print(f"Calculation error occurred: {e}", file=sys.stderr)
        return 0.0

def main():
    # Hard-coded sample values simulating reading from a file
    volume_measurements = [15.5, "20", "# This is a comment\n", "-3.7", "", "invalid_data"]
    
    try:
        total_volume = calculate_total_volumes(volume_measurements)
        
        if not isinstance(total_volume, float):
            print("Error in calculation result type.")
            return
            
        # Output the final calculated volume with 2 decimal places for clarity
        print(f"Total Volume: {total_volume:.2f}")
        
    except Exception as e:
        print(f"An unexpected error occurred while processing volumes: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()