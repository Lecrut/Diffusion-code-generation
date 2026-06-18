import argparse
from statistics import mean, stdev

def calculate_statistics(volumes):
    """Calculate arithmetic mean and standard deviation efficiently."""
    if len(volumes) < 2:
        return None, None
    
    m = sum(volumes) / len(volumes)
    
    # Efficient calculation of variance using the computational formula
    sq_sum = sum(x * x for x in volumes)
    n = len(volumes)
    var_sq = (sq_sum - (m ** 2) * n) / ((n - 1) * n) if n > 0 else 0
    
    std_dev = float(var_sq) ** 0.5 if var_sq >= 0 else 0.0
    
    return m, std_dev

def main():
    parser = argparse.ArgumentParser(description="Calculate mean and standard deviation of volume values.")
    
    # Define a list of sample volumes to use when no arguments are provided
    default_values = [10.5, 20.3, 18.7, 25.1, 19.4]
    
    parser.add_argument(
        '--volumes', 
        nargs='+', 
        type=float, 
        help='List of volume values to process.'
    )
    
    args = parser.parse_args()
    
    # If no arguments provided or empty list, use hard-coded sample values
    if not args.volumes:
        volumes = default_values.copy()
    else:
        try:
            volumes = [float(x) for x in args.volumes]
        except ValueError as e:
            print(f"Error converting input to float: {e}")
            return
    
    result_mean, result_std_dev = calculate_statistics(volumes)
    
    if result_mean is None:
        print("Insufficient data points. Need at least 2 values.")
    else:
        print(f"Arithmetic Mean: {result_mean:.4f}")
        print(f"Standard Deviation: {result_std_dev:.4f}" if result_std_dev != 0 else "Standard Deviation: N/A (only one value)")

if __name__ == '__main__':
    main()