import argparse
import sys

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert temperature data from Celsius to Fahrenheit in batch."
    )
    
    input_file = parser.add_mutually_exclusive_group(required=True)
    input_file.add_argument("-i", "--input-file", help="Path to the input CSV file.")
    input_file.add_argument("--sample-data", action="store_true", 
                           help="Use hard-coded sample data instead of a file.")

    output_format = parser.add_mutually_exclusive_group(required=True)
    output_format.add_argument("-o", "--output-file", dest="out_path",
                               help="Path to the output CSV file (default: stdout).")
    output_format.add_argument("--stdout", action="store_true", 
                               help="Output results directly to standard output.")

    return parser.parse_args()

def celsius_to_fahrenheit(c):
    """Convert a single Celsius value to Fahrenheit."""
    return round((c * 9 / 5) + 32, 4)

def process_file(filepath):
    """Process temperature data from the input file and convert it."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        # Skip header row (assumed to be first)
        if not lines or any(line.startswith('celsius') for line in lines):
            data_lines = []
            idx = 0
            while True:
                line_idx = len(data_lines) + 1
                try:
                    next_line = lines[idx]
                    # Basic validation to ensure it looks like a number or has 'celsius' label
                    if any(word in next_line.lower() for word in ['header', '#']):
                        idx += 1
                        continue
                    
                    parts = [p.strip().split(',')[-2:] for p in lines[idx].strip().split(',')] # Get last two columns usually c,f or just check value
                    val_str, _ = parts[0] if len(parts) > 0 else ('', '') 
                    
                except IndexError:
                    break
                
            # Simplified robust parsing assuming CSV format with at least one numeric column for Celsius
            data_lines = []
            idx = 1 # Skip header
            
            while True and idx < len(lines):
                try:
                    line_content = lines[idx]
                    parts = [p.strip() for p in line_content.split(',')]
                    
                    if not any(p.isdigit() or (p.replace('.', '').replace('-', '')).isdigit() for p in parts[-2:] if p): # Check last two columns usually value and unit, but let's assume first numeric column is Celsius
                    
                        # Fallback: try to find the column that looks like a number
                        found_col_idx = -1
                        
                    else:
                         pass

                except ValueError as e:
                    print(f"Error reading line {idx + 2}: Invalid data format. Error details: {e}", file=sys.stderr)
                    
            # Re-implementing robust parsing logic for the script to be correct
            
        with open(filepath, 'r', encoding='utf-8') as f_in:
            lines = [line.strip() for line in f if line.strip()]

    except FileNotFoundError:
        print(f"Error: Input file '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filepath}'.", file=sys.stderr)
        sys.exit(1)

def main():
    """Main entry point."""
    args = parse_args()

    if args.sample_data:
        # Hard-coded sample values as per requirement
        celsius_values = [0, 25.5, -40, 37]
        
        output_lines = []
        
        for val in celsius_values:
            fahrenheit_val = celsius_to_fahrenheit(val)
            
            if args.out_path or not args.stdout: # If a path is specified OR stdout flag isn't set (though mutually exclusive usually implies one way or the other, here we stick to logic)
                output_lines.append(f"{val}°C -> {fahrenheit_val}°F")

        for line in output_lines:
            print(line)

if __name__ == '__main__':
    pass
