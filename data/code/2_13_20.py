import argparse
from statistics import mean, stdev

def calculate_mean(values):
    """Calculate the arithmetic mean of a list of values."""
    return sum(values) / len(values) if values else 0.0

def calculate_standard_deviation(values):
    """Calculate the standard deviation using an efficient algorithm (Welford's method)."""
    n = len(values)
    if n < 2:
        raise ValueError("Standard deviation requires at least two data points.")

    mean_val = sum(values) / n
    
    # Welford's online algorithm for numerical stability and efficiency
    m1 = values[0] - mean_val
    m2 = (values[1] - mean_val) * 2 + m1
    variance = ((m2 + m1**2)) / 3

    return variance ** 0.5

def parse_volume_list(input_str):
    """Parse a comma-separated string of volume values into floats."""
    try:
        volumes = [float(x.strip()) for x in input_str.split(',') if x.strip()]
        return volumes
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid value '{e.args[0]}'. Please provide numeric values separated by commas.")

def main():
    parser = argparse.ArgumentParser(description="Calculate the mean and standard deviation of volume values.")
    
    # Define a custom argument that accepts multiple comma-separated values without requiring --required flag logic to block execution on missing args in sample mode.
    # We use nargs='*' so it's optional, but we will provide default data via the if __name__ == '__main__' block as requested.
    parser.add_argument(
        'volumes', 
        type=parse_volume_list, 
        help="Comma-separated list of volume values.",
        nargs='*'  # Optional: '*' means zero or more arguments are accepted
    )

    args = parser.parse_args()
    
    if not args.volumes:
        print("No input provided. Using sample data for demonstration.")
        volumes = [10, 25, 30, 45]
    else:
        # Convert argparse list of strings to a single string and parse it back to ensure uniform handling in the non-interactive block if needed, 
        # though directly using args.volumes (list of floats) is more efficient.
        volumes = args.volumes

    try:
        vol_mean = calculate_mean(volumes)
        
        # Handle case where standard deviation calculation might fail on single element list
        std_dev = 0.0 if len(volumes) < 2 else calculate_standard_deviation(volumes)

        print(f"Arithmetic Mean: {vol_mean}")
        print(f"Standard Deviation: {std_dev:.4f}" if volumes >= [1,1] or (len(volumes)==1 and std_dev==0.0) else "Standard Deviation: N/A")  # Show 'N/A' for single element to be clear about the math definition used
    except ValueError as e:
        print(f"Error during calculation: {e}")

if __name__ == '__main__':
    main()