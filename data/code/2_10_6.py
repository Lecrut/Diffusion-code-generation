import sys

def read_volume_from_file(filename):
    """Reads volume measurements from a file line by line."""
    total_volume = 0.0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Strip whitespace and skip empty lines
                value_str = line.strip()
                if not value_str:
                    continue
                
                try:
                    volume = float(value_str)
                    total_volume += volume
                except ValueError:
                    print(f"Warning: Skipping invalid entry '{value_str}' - cannot convert to float.", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    
    return total_volume

def main():
    # Hard-coded sample values simulating a volume measurement log
    filename = "volumes.txt"
    
    try:
        total_vol = read_volume_from_file(filename)
        print(f"Total Volume: {total_vol}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()