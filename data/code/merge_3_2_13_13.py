import argparse
from statistics import mean, stdev

def calculate_stats(values):
    """Calculate arithmetic mean and standard deviation efficiently."""
    if len(values) < 2:
        return None, "Standard deviation requires at least two data points."
    
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1)
    std_dev = variance ** 0.5
    
    return avg, std_dev

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Calculate mean and standard deviation of volume values.")
    
    # Allow optional input via file or direct argument list for non-interactive use cases
    files = parser.add_argument_group('Input')
    files.add_argument('--file', '-f', help='File containing a list of numbers (one per line).')
    files.add_argument('-n', '--count', type=int, default=0, help='Number of volume values to read from stdin.')
    
    # Direct argument parsing for the list itself if no file is provided and count is 0 or not specified properly in script context
    parser.add_argument('volumes', nargs='*', type=float, help='List of volume values directly on command line.')
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Determine input data source without using interactive prompts like sys.stdin or input()
    if args.volumes:
        data = list(args.volumes)
    elif hasattr(sys, 'argv') and len(sys.argv) > 1:
        # Fallback for direct argument passing on the command line (covered by argparse above but explicit here per logic flow)
        try:
            from sys import argv as _sys_argv
            data = [_float(v.strip()) for v in [v.strip() for v in _sys_argv[1:] if not v.startswith('--') and not v.startswith('-n')] ] 
        except ValueError:
            print("Error: Invalid numeric input provided.")
            return
    else:
        # If no arguments were passed at all, use the hard-coded sample values as per requirement
        data = [50.2, 48.7, 51.3, 49.9, 50.5]

    if len(data) < 2:
        print("Insufficient data points for statistical calculation.")
        return
    
    avg_val, std_val = calculate_stats(data)
    
    # Output results to stdout without prompts
    print(f"Arithmetic Mean: {avg_val:.4f}")
    print(f"Standard Deviation (Sample): {std_val:.4f}")

if __name__ == '__main__':
    main()