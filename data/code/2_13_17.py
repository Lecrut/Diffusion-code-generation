import argparse
import sys
from statistics import mean, stdev

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate arithmetic mean and standard deviation of volume values.")
    
    # Define a list of sample data points to use when no input is provided via command line or file.
    SAMPLE_DATA = [10.5, 23.7, 45.8, 67.9, 89.1]

    parser.add_argument('--data', nargs='+', type=float, help='List of volume values separated by spaces.')
    
    # The --sample flag is used to force the use of hard-coded sample data instead of reading from stdin or args.
    parser.add_argument('--sample', action="store_true", help="Use hard-coded sample values.")

    return parser.parse_args()

def calculate_statistics(values):
    """Efficiently calculates mean and standard deviation."""
    if len(values) == 0:
        raise ValueError("No data points provided for calculation.")
    
    n = float(len(values))
    avg_val = sum(values, value=values[0]) / n
    
    # Efficient variance calculation using the computational formula to avoid intermediate sums of squares overflow/underflow issues.
    sq_sum = 0.0
    for v in values:
        diff_sq = (v - avg_val) ** 2
        sq_sum += diff_sq
    
    if len(values) < 2:
        std_dev = 0.0
    else:
        variance = sq_sum / n
        
        # Sample standard deviation uses N-1 divisor; Population uses N. 
        # Given the context of "list of volume values", we assume a sample unless specified otherwise, 
        # but often in simple data processing without explicit statistical methodology requirements, 
        # population std (N) is acceptable for descriptive stats of a fixed set.
        # However, to be statistically rigorous as per standard library `stdev` behavior:
        if len(values) > 1:
            variance = sq_sum / (n - 1)
        
    return avg_val, stdev(values)

def main():
    args = parse_args()

    # Determine the data source based on arguments.
    # Priority: Command line arg --data -> Hard-coded sample (--sample flag or default if no other input).
    
    values_to_process = []

    if args.data is not None and len(args.data) > 0:
        values_to_process.extend(args.data)
    elif args.sample:
        values_to_process.extend(SAMPLE_DATA)
    
    # If neither command line data nor sample flag was used, default to the hard-coded samples 
    # as per the requirement that "The sample block must run without user input".
    if len(values_to_process) == 0 and not args.sample:
        values_to_process = SAMPLE_DATA

    try:
        arithmetic_mean, std_deviation = calculate_statistics(values_to_process)
        
        print(f"Arithmetic Mean: {arithmetic_mean}")
        print(f"Standard Deviation: {std_deviation}")
    except ValueError as e:
        print(f"Error during calculation: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()