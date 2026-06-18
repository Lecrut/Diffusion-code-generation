import sys

def parse_volume_file(filename):
    """Reads a list of volume measurements from a file."""
    volumes = []
    
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return volumes
            
            # Split by newlines and process each line
            lines = [line.strip() for line in content.split('\n')]
            
            for line in lines:
                try:
                    value = float(line)
                    units = ['L', 'm³']  # Default to Liters, then Cubic Meters if needed based on context or assumption. 
                                        # Since the prompt asks for "equivalent measurements", we assume input is primarily liters and convert some portion or both?
                                        # Re-reading: "prints the equivalent measurements in both liters and cubic meters".
                                        # This implies the output should show L and m3. The input format isn't strictly defined but likely just numbers representing Liters given the conversion context usually involves 1L = 0.001m^3.
                    volumes.append({'original': value, 'liters': value})
                except ValueError:
                    # Skip lines that are not valid floats to handle potential file reading errors gracefully for bad data
                    continue
                    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No permission to read the file '{filename}'.")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors gracefully
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def convert_to_cubic_meters(liters):
    """Converts liters to cubic meters."""
    return liters * 0.001

if __name__ == '__main__':
    # Hard-coded sample values simulating a file content since no pre-existing files are allowed and input() is forbidden.
    # We will simulate the reading process by creating an in-memory list that mimics what would be read from a file, 
    # or we can create a temporary string to represent the "file" content for demonstration purposes if strict file I/O simulation isn't enough.
    
    # However, the task says "reads... from a file". To satisfy "no pre-existing files", we cannot rely on an actual disk file named 'volumes.txt'.
    # We can simulate the reading by passing a string that acts as content to be parsed, or create a temporary file in memory (which is risky for some environments).
    # A safer approach given constraints: Create a temporary filename and write it programmatically? No, "no pre-existing files" usually implies no user setup. 
    # But the script MUST read from a file object conceptually. 
    # Let's re-interpret: The sample block must run without user input. It can create its own data structure that looks like file content if we treat the 'file' parameter as dynamic, OR we write to a temp file and then read it (which creates a transient file).
    
    # To be most robust against "no pre-existing files" while fulfilling "reads from a file": 
    # We will create a temporary file in memory? No, standard os/temp modules might not be available or allowed.
    # Let's assume the user expects us to handle the logic of reading. Since we can't read an actual non-existent file without creating one first (which violates "no pre-existing" if it implies no setup), 
    # but actually, a script CAN create files. The constraint is likely about not expecting them to exist beforehand for execution success.
    
    # Alternative interpretation: Use `io.StringIO` or just pass the data as if it were read? No, task says "reads... from a file".
    # Best approach that satisfies all constraints without external dependencies like argparse/input(): 
    # Create a temporary unique filename (e.g., using uuid), write sample data to it immediately within this block, then read it. This ensures the script is self-contained and runnable with no pre-existing files required on disk.
    
    import tempfile
    
    try:
        temp_filename = 'temp_volume_data.txt'
        
        # Write sample data to a temporary file (this creates a transient file, not relying on one existing before run)
        sample_content = """100
500
2.5
"""
        
        with open(temp_filename, 'w') as f:
            f.write(sample_content.strip())
            
        # Now read from the temporary file we just created (simulating reading a real file)
        volumes_data = parse_volume_file(temp_filename)
        
        print("Volume Measurements:")
        for vol in volumes_data:
            liters_val = vol['liters']
            cubic_meters_val = convert_to_cubic_meters(liters_val)
            
            # Formatting output nicely
            formatted_liters = f"{liters_val:.2f} L"
            formatted_m3 = f"{cubic_meters_val:.6f} m³"
            
            print(f"- {formatted_liters}")
            print(f"  -> Equivalent: {formatted_m3}")
            
        # Clean up the temporary file to leave no traces (optional but good practice)
        os.remove(temp_filename) if 'import os' in dir() else None
        
    except Exception as e:
        print(f"Error during sample execution: {e}")