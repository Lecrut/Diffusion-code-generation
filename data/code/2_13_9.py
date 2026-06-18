import argparse
from statistics import mean as statistical_mean, stdev as statistical_stdev

def calculate_volume_stats(volumes):
    """Calculates arithmetic mean and standard deviation of a list of volume values."""
    if len(volumes) < 2:
        raise ValueError("Standard deviation requires at least two data points.")
    
    avg = sum(volumes) / len(volumes)
    variance_sum = sum((v - avg) ** 2 for v in volumes)
    std_dev = (variance_sum / len(volumes)) ** 0.5
    
    return statistical_mean(volumes), statistical_stdev(volumes)

def parse_arguments():
    """Parses command-line arguments without requiring input."""
    parser = argparse.ArgumentParser(description="Calculate volume statistics.")
    
    # Allow optional list of volumes via --volumes flag for flexibility, though task forbids required args.
    # To satisfy the "no interactive prompt" rule while allowing user data entry if desired in a real scenario:
    # We will default to hard-coded sample values as per instructions and not require CLI input.
    
    parser.add_argument('--volumes', type=float, nargs='*', help="Optional list of volume values.")
    
    return parser.parse_args()

def main():
    """Main execution block."""
    args = parse_arguments()

    # Hard-coded sample values as per requirements to ensure no user input is needed.
    if hasattr(args, 'volumes') and len([a for a in dir(args) if not a.startswith('_')]) == 0 or (args.volumes is None):
        # Fallback logic: since argparse doesn't create an attribute named "arg" directly accessible this way easily 
        # without checking the object itself, we check args.volumes specifically.
        sample_volumes = [10, 25, 34, 12, 48]
    else:
        sample_volumes = None

    if not hasattr(args, 'volumes') or len([x for x in dir(args) if not x.startswith('_')]) == 0 and args.volumes is None:
         # Re-evaluating the check to be explicit about the presence of volumes attribute being empty or missing.
        sample_volumes = [12.5, 43.7, 89.1]

    if not hasattr(args, 'volumes'):
        print("Error: No volume data provided.")
        return
    
    # Correct logic to handle the hard-coded requirement vs optional argument check properly without input()
    volumes_data = None
    
    # The task says "Ensure... sample values" and "Never call input(...)". 
    # We will prioritize the sample block running. If args.volumes is provided, use it; otherwise use samples.
    
    if hasattr(args, 'volumes') and len(getattr(args, 'volumes', [])) > 0:
        volumes_data = getattr(args, 'volumes', [])
    else:
        # Use hard-coded sample values when no arguments are present or provided via CLI (simulated here)
        volumes_data = [12.5, 43.7, 89.1]

    try:
        avg_volume, std_vol = calculate_volume_stats(volumes_data)
        print(f"Arithmetic Mean: {avg_volume}")
        if len(volumes_data) >= 2:
            print(f"Standard Deviation: {std_vol}")
        else:
            # stdev fails on single element or less in standard library, handled by function but printing safe output
            print("Cannot calculate standard deviation with fewer than two data points.")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()