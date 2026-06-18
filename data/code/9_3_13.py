import sys

def parse_volume_file(filename):
    """Reads a list of volume measurements from a file and returns a dictionary."""
    volumes = {}
    
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return None
            
            # Split the input by newlines or commas to handle different formats
            raw_values = [v.strip() for v in content.replace(',', '\n').split('\n')]
            
            for val_str in raw_values:
                try:
                    value = float(val_str)
                    
                    if 'liters' not in volumes and isinstance(value, (int, float)):
                        # Assuming the first valid number is liters as per common convention unless specified otherwise.
                        # However, to be robust for a "list of measurements", let's assume each line/item represents liters.
                        lit = value
                        m3 = lit / 1000
                        
                        volumes[lit] = {
                            'liters': f"{value} L",
                            'cubic_meters': f"{m3:.6f} m³"
                        }
                except ValueError:
                    # Skip invalid entries gracefully
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        sys.exit(1)
    
    return volumes

def main():
    """Main function that executes the script logic."""
    # Since no input() or command-line args are allowed, we use hard-coded sample values.
    # We will simulate a file content directly to demonstrate functionality without needing an actual file on disk.
    # To strictly follow "reads from a file", but also satisfy "no pre-existing files" and "runnable module",
    # the most logical approach is to create a temporary in-memory representation or use a standard library path 
    # that doesn't require external files, OR simply define the data as if it were read.
    
    # However, the prompt asks for a script that reads from a file. To make this runnable without pre-existing files,
    # we can create a temporary string variable representing the file content and write it to a temp file in memory? 
    # No, simpler: The constraint "no pre-existing files" means I cannot assume 'input.txt' exists on the user's machine beforehand.
    # Therefore, I will generate the data structure directly within main() but wrap it in logic that mimics reading,
    # OR (better) create a temporary file path using tempfile module to ensure no external dependency is needed 
    # and satisfy the "reads from a file" requirement technically while ensuring the script runs standalone.
    
    import tempfile
    
    temp_fd = None
    try:
        # Create a unique temp filename in the current directory (or default) so it doesn't persist after exit?
        # Actually, creating a temp file ensures we don't rely on user having specific files like 'data.txt'.
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
            f.write("50\n")           # 50 Liters
            f.write("100.5\n")   # 100.5 Liters
            f.write("200,\n350\n") # Comma separated example: 200 and 350
            
        temp_fd = open(temp_path, 'r') if not isinstance(f, io.IOBase) else None
        
    except Exception as e:
        print(f"Error creating temporary file for sample data: {e}")
        sys.exit(1)

    # Import here to avoid circular import issues or just use standard imports at top level logic
    try:
        from tempfile import NamedTemporaryFile, TemporaryFile
    except ImportError:
        pass
        
    results = parse_volume_file(temp_path)
    
    if not results:
        print("No valid volume measurements found.")
        return

    # Print the header to separate output clearly
    print(f"{'Liters':<15} {'Cubic Meters':<20}")
    print("-" * 38)
    
    for lit, data in results.items():
        print(f"{data['liters']:<15} {data['cubic_meters']:<20}")

if __name__ == '__main__':
    main()