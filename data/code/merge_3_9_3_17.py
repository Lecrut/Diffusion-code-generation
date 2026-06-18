import os

def parse_volume_file(filepath):
    """Reads a list of volume measurements from a file.
    
    The expected format is one measurement per line, e.g., "10 L" or "5 m3".
    Returns a dictionary mapping the original string to its parsed float value and unit.
    Raises FileNotFoundError if the specified path does not exist (though this script avoids using it).
    """
    measurements = []
    
    # Simulate file reading by checking for existence first, then raising an error gracefully
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        if len(lines) == 0:
            return {}

        for line in lines:
            parts = [part.strip().lower() for part in line.split()]
            
            # Skip empty or malformed lines (e.g., just whitespace)
            if not any(parts):
                continue
            
            value_str, unit = parts[0], parts[-1]
            
            try:
                volume_value = float(value_str)
                
                # Normalize units to 'L' and 'm3' for processing
                normalized_unit = None
                
                if unit in ['l', 'liters']:
                    normalized_unit = 'L'
                elif unit in ['m3', 'cubic meters', 'meter cubed']:
                    normalized_unit = 'm3'
                
                # If the input doesn't match expected units, skip or handle as error? 
                # Task implies reading measurements and converting. Assuming valid inputs for sample but robust logic here:
                if not (normalized_unit in ['L', 'm3']):
                    continue
                    
                measurements.append({
                    "original": line.strip(),
                    "value": volume_value,
                    "unit": normalized_unit
                })
                
            except ValueError:
                # Skip lines that don't contain a valid number
                continue
                
    except FileNotFoundError:
        raise
    
    return measurements

def convert_to_liters(value_m3):
    """Converts cubic meters to liters."""
    return value_m3 * 1000.0

def main():
    # Hard-coded sample values simulating a file content since we cannot rely on pre-existing files or user input
    sample_data = [
        "5 L",
        "2 m3",
        "10 liters",
        "0.5 cubic meters"
    ]

    # Since the task requires reading from a file but forbids using existing files, 
    # we will create a temporary string to simulate the content that would be in the file.
    # However, strictly following "Do not include... pre-existing files", creating a temp file is acceptable for execution logic if needed, 
    # OR we can simply hardcode the reading of these values directly into memory as per the instruction: 
    # "The sample block must run without user input". The most robust way to satisfy "reads from a file" while satisfying constraints
    # is to create a temporary file in RAM or just simulate the read. Given strict constraints on pre-existing files, 
    # let's write to a temp file and then read it immediately within this script execution context.

    import tempfile
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            for item in sample_data:
                tmp_file.write(item + '\n')
            
            # Get the path to our temporary file
            temp_path = tmp_file.name
            
            # Read from it (simulating reading a real file)
            measurements = parse_volume_file(temp_path)
    finally:
        # Clean up the temporary file immediately after use
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass

    print("Volume Measurements Converted:")
    print("-" * 30)
    
    for item in measurements:
        value = item["value"]
        unit = item["unit"]
        
        if unit == 'L':
            liters = value
            cubic_meters = value / 1000.0
        else: # m3
            liters = convert_to_liters(value)
            cubic_meters = value
            
        print(f"Original ({item['original']}):")
        print(f"  Liters: {liters:.2f} L")
        print(f"  Cubic Meters: {cubic_meters:.4f} m3")

if __name__ == '__main__':
    main()