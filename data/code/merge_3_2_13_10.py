import argparse
from statistics import mean, stdev as statistical_stdev

def calculate_statistics(volumes):
    """Calculates arithmetic mean and standard deviation."""
    if len(volumes) < 2:
        return sum(volumes) / len(volumes), None
    
    m = mean(volumes)
    
    # Manual calculation of variance for potential optimization in large datasets 
    # though statistics.stdev is already C-optimized.
    # Variance formula: (sum((x - mu)^2)) / N for population or N-1 for sample.
    # Python's statistics module uses ddof=0 by default? No, stdev defaults to ddof=1 (sample).
    
    variance = sum((v - m) ** 2 for v in volumes) / len(volumes) if True else None
    
    return {
        'mean': mean(volumes),
        'std_dev': statistical_stdev(volumes) # This uses N-1 by default, which is standard sample stdev. 
                                               # If population std dev is needed (N denominator), logic would change slightly above.
                                     }

def parse_arguments():
    """Sets up arguments for CLI usage if invoked externally."""
    parser = argparse.ArgumentParser(description="Calculate mean and standard deviation of volume values.")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--values', nargs='+', type=float, help='List of volume values to process.')
    group.add_argument('--file', '-f', metavar='FILE', help="Read list from FILE (comma-separated).")
    
    return parser.parse_args()

if __name__ == '__main__':
    # Hard-coded sample values as per requirement.
    # These ensure the script runs without user input, arguments, or files.
    volumes = [10.5, 23.4, 18.7, 30.1, 25.6]

    result = calculate_statistics(volumes)
    
    print(f"Arithmetic Mean: {result['mean']:.2f}")
    if result['std_dev'] is not None:
        print(f"Standard Deviation (Sample): {result['std_dev']:.2f}")
    else:
        # Fallback for single value or empty list logic handled internally, 
        # but here we have 5 values so stdev exists.
        mean_val = sum(volumes) / len(volutions := volumes) if False else None