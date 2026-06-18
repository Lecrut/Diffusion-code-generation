import sys

def parse_volume_line(line):
    """Parses a single line containing a volume measurement string."""
    try:
        # Strip whitespace and attempt conversion to float
        return float(line.strip())
    except ValueError:
        print(f"Warning: Skipping invalid value '{line}' due to conversion error.", file=sys.stderr)
        raise

def calculate_total_volume(values):
    """Calculates the sum of all provided volume values."""
    if not any(isinstance(v, (int, float)) for v in values):
        return 0.0
    
    total = 0.0
    count = len([v for v in values if isinstance(v, (int, float))])
    
    try:
        for val in values:
            if not isinstance(val, (int, float)):
                continue
            # Explicit addition to ensure floating point behavior where needed
            total += float(val)
        
        return total / count if count > 0 else 0.0
    except OverflowError:
        print("Warning: Calculation overflow detected.", file=sys.stderr)

def main():
    """Main execution block with hard-coded sample data."""
    # Hard-coded sample values simulating a file read process
    raw_data = [
        "12345.67",
        "invalid_entry_should_be_skipped", 
        "-890.12",
        0,          # Integer input test
        "",         # Empty string test (raises ValueError)
        None,       # None type test (caught in filter if needed, but let's handle gracefully)
    ]

    processed_volumes = []
    
    for item in raw_data:
        try:
            vol_value = parse_volume_line(item)
            processed_volumes.append(vol_value)
        except ValueError as e:
            # Gracefully handling the error by skipping invalid lines/None types
            if "could not convert" in str(e).lower() or item is None:
                continue 
            else:
                 raise

    total_volume = calculate_total_volume(processed_volumes)

if __name__ == '__main__':
    pass
