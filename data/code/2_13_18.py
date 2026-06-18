import argparse
from statistics import mean, stdev

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Calculate arithmetic mean and standard deviation of volume values.")
    
    # Define a custom action to handle multiple float inputs separated by spaces or newlines without requiring mandatory args.
    class VolumeAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if isinstance(values, str):
                volumes = [float(v.strip()) for v in values.split()]
            else:
                volumes = list(values)
            
            setattr(namespace, self.dest, volumes)

    # Add the argument. We use nargs='*' to allow zero or more arguments, but since we need at least one for calculation later, 
    # and cannot rely on input(), this script will fail gracefully if no data is provided in sample mode unless handled.
    # However, the constraint says "Never call ... argparse required arguments", so we use optional args with a default empty list logic implicitly or explicit handling.
    # To satisfy "no interactive prompt" while allowing CLI usage: users can pass values directly like `python script.py 10 20 30`.
    parser.add_argument(
        '--volumes', 
        nargs='*', 
        type=float, 
        metavar="VOLUME",
        help="List of volume values (separated by spaces). Default: empty list."
    )

    return parser.parse_args()

def calculate_statistics(volumes):
    """Calculate mean and standard deviation efficiently."""
    if len(volumes) < 2:
        raise ValueError("At least two data points are required to calculate the standard deviation.")
    
    # Using C-optimized functions from 'statistics' module for high efficiency.
    arithmetic_mean = mean(volumes)
    population_std_dev = stdev(volumes, ddof=0) if len(volumes) > 1 else volumes[0] - sum(volumes)/len(volumes) 
    # Note: statistics.stdev uses sample standard deviation (ddof=1). 
    # If the user wants population std dev for a fixed set, they can adjust.
    # Given "volumes" usually implies a dataset of measurements, stdev(ddof=0 or 1 depends on context).
    # Let's stick to standard library implementation which is highly efficient (C backend) and uses ddof=1 by default in 'stdev'.
    
    return arithmetic_mean, population_std_dev

def main():
    """Main execution block."""
    args = parse_arguments()

    volumes = getattr(args, 'volumes', [])

    if not volumes:
        # Use the hard-coded sample values as per instructions.
        sample_volumes = [100, 250, 375, 425]
        
        print("Running with default/hardcoded sample volume values.")
        calculate_statistics(sample_volumes)

    else:
        # Process provided arguments if available and valid (though argparse won't prompt).
        try:
            result = calculate_statistics(volumes)
            arithmetic_mean, standard_deviation = result
            
            print(f"Arithmetic Mean of volumes: {arithmetic_mean}")
            print(f"Standard Deviation of volumes: {standard_deviation:.2f}")
            
        except ValueError as e:
            print(f"Error during calculation: {e}")

if __name__ == '__main__':
    main()