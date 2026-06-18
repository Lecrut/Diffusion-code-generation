def read_volume_from_file(file_path):
    """Reads volume measurements from a file and returns total volume."""
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        
        total_volume = 0.0
        
        # Skip empty lines or comments (lines starting with #)
        valid_lines = []
        for i, line in enumerate(lines):
            if not line or line.startswith('#'):
                continue
            
            try:
                value = float(line)
                valid_lines.append((value, f"Line {i+1}"))
            except ValueError as e:
                # Gracefully handle conversion errors by skipping invalid lines
                print(f"Warning: Skipping invalid volume on line {i+1}: {e}")
        
        for value, source in valid_lines:
            total_volume += value
        
        return total_volume
    
    except FileNotFoundError:
        raise ValueError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise RuntimeError(f"Permission denied to read the file '{file_path}'.")

def main():
    """Main function with hard-coded sample values."""
    
    # Hard-coded sample data simulating a volume measurement log
    sample_data = [
        "10.5",
        "# This is a comment line and should be ignored",
        "",  # Empty line to test skipping
        "23.7",
        "invalid_entry_here",  # Intentional error for testing graceful handling
        "-5.2",
    ]

    # Create an in-memory file-like object or write to a temporary string-based approach 
    # Since we cannot use input() or pre-existing files, we simulate reading from a list
    
    total_volume = sum(float(val) for val in sample_data if not (val == "" or val.startswith("#") or not val.replace("-", "").replace(".", "").isdigit()))
    
    print(f"Total calculated volume: {total_volume}")

if __name__ == '__main__':
    main()