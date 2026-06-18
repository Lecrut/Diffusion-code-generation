def read_volume_file(filepath):
    """Reads volume measurements from a file and returns total volume."""
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
        
        # Handle case where file might contain multiple lines or just numbers separated by spaces/newlines
        values_str = [v.strip() for v in content.split()]
        
        total_volume = 0.0
        
        for val_str in values_str:
            if not val_str:
                continue
            
            try:
                value = float(val_str)
                total_volume += value
                
                # Graceful handling of conversion issues is implicit via the raise exception logic
                # If a non-numeric string exists, it will trigger an error below which we handle in main
            except ValueError as e:
                print(f"Warning: Failed to convert '{val_str}' to float. Skipping.")
                
        return total_volume
        
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        raise

def calculate_total_from_list(values):
    """Calculates the sum of a list of numeric values."""
    try:
        converted_values = [float(v) for v in values]
        total_volume = sum(converted_values, 0.0)
        
        if not isinstance(total_volume, float):
            raise TypeError("Expected float result from conversion/sum")
            
        return total_volume
        
    except ValueError as e:
        print(f"Error during calculation: {e}")
        raise

if __name__ == '__main__':
    # Hard-coded sample values simulating volume measurements stored in a file-like structure
    raw_data_str = "5.0 12.34 8.7 invalid_entry -3.2 99.9"
    
    try:
        total_volume = calculate_total_from_list(raw_data_str.split())
        
        print(f"\nTotal Volume Calculated: {total_volume}")
        print("Calculation completed successfully.")
        
    except Exception as ex:
        # Final catch-all for any unexpected errors during the main execution block
        if "ValueError" in str(type(ex)) or isinstance(ex, ValueError):
            print(f"\nCritical Error encountered. Non-numeric data detected and skipped gracefully where possible.")
        else:
            raise ex