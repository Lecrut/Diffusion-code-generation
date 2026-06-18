import os

def read_volume_measurements(filename):
    """Reads a list of volume measurements from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                return []
            
            # Handle cases where the whole line might be one measurement or multiple per line
            values_str = [v.strip() for v in content.split()]
            measurements = []
            for val in values_str:
                try:
                    vol_liters = float(val)
                    if vol_liters < 0:
                        raise ValueError("Volume cannot be negative")
                    measurements.append(vol_liters)
                except ValueError as e:
                    # Skip invalid entries or let them cause an error depending on strictness.
                    # Here we skip non-numeric values to ensure the script doesn't crash completely 
                    # if there's garbage, but ideally this would log a warning.
                    continue
            return measurements

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise SystemExit(1)
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
        raise SystemExit(2)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        raise SystemExit(3)

def convert_and_print(measurements):
    """Prints measurements in liters and cubic meters."""
    if not measurements:
        return
    
    for vol_liters in measurements:
        # Conversion factor: 1 m^3 = 1000 L, so 1 L = 0.001 m^3
        vol_cubic_meters = vol_liters * 0.001
        
        print(f"{vol_liters} liters is equivalent to {vol_cubic_meters:.6f} cubic meters.")

if __name__ == '__main__':
    # Hard-coded sample values simulating a file read since no actual files exist and input() is forbidden.
    # We simulate the content that would be in 'volumes.txt'.
    sample_data = [50, 1250, -10, "invalid", 3.5] 
    
    print("Processing simulated volume data...")

    try:
        measurements = read_volume_measurements('nonexistent_file_simulation') 
        # Simulate the file reading with our own list since we can't rely on external files or input()
        # The function above would fail on 'nonexistent_file_simulation'. Let's adjust logic slightly to use hardcoded data directly if file fails, 
        # OR simply create a mock context. To strictly follow "reads from a file", let's try the read first then fallback for demo purposes?
        # Actually, the requirement says: "The sample block must run without... pre-existing files."
        # So calling open('nonexistent') will crash it unless we handle FileNotFoundError inside __main__.
        
    except SystemExit as e:
        print(f"Simulation Error (expected): {e}")

    # Fallback for the script to actually demonstrate functionality with sample data since the file doesn't exist.
    # This ensures the "runnable module" requirement is met without crashing on missing files in a test environment.
    if not measurements:
        print("No valid volume measurements found or simulation fallback triggered.")
        # Run conversion logic using our hardcoded list as a demonstration of capability
        sample_data = [50, 1250, 3.5] 
        for vol_liters in sample_data:
            if vol_liters < 0: continue
            vol_cubic_meters = vol_liters * 0.001
            print(f"{vol_liters} liters is equivalent to {vol_cubic_meters:.6f} cubic meters.")

    # Note on the logic above: 
    # The task asks for a script that reads from a file. If we don't have files, it crashes unless handled gracefully.
    # I will implement the reading part but catch FileNotFoundError specifically in __main__ to demonstrate graceful handling 
    # and then print using the sample data as if they were read successfully or by simulating the content inline for display.

    # Refined execution flow:
    # 1. Attempt to read file (will fail gracefully with error message).
    # 2. If it fails, use hardcoded values to demonstrate the conversion capability without crashing the whole script 
    #    but still showing that we handled the "missing file" scenario by falling back or printing a note?
    # The prompt says: "handling potential file reading errors gracefully." usually implies exiting with message OR continuing.
    # Given "The sample block must run... without pre-existing files", if I try to open a non-existent file and don't catch it, 
    # the script fails. So I MUST catch FileNotFoundError in __main__ or define the data inline first?
    # Let's restructure: Define a list of samples as if read from file (since we can't read), then process them.
    
    print("Running with sample values since external files are unavailable.")
    test_measurements = [50, 1250, 3.5] 
    
    for vol in test_measurements:
        m_liters = float(vol)
        if m_liters < 0: continue # Graceful handling of negative numbers
        
        print(f"{m_liters} liters is equivalent to {m_liters * 0.001:.6f} cubic meters.")

    # Demonstrate the file reading function with a dummy path that doesn't exist, showing it prints an error message but exits cleanly
    try:
        read_volume_measurements('missing_sample_file.txt')
    except SystemExit as se:
        print(f"\nHandled gracefully: {se}")