import argparse
from statistics import mean as calculate_mean, stdev as calculate_std_dev

def parse_arguments():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description="Calculate arithmetic mean and standard deviation of volume values.")
    parser.add_argument("volumes", nargs="+", type=float, help="List of volume values to process.")
    
    # Use optional '--use-sample' flag instead of required args if needed for sample block logic later.
    # However, since the task forbids calling input() or sys.stdin and requires no interactive prompts:
    # We will handle both CLI usage (if provided) and the hard-coded sample execution within main().
    
    return parser.parse_args()

def calculate_statistics(values):
    """Calculate mean and standard deviation efficiently."""
    if len(values) < 2:
        raise ValueError("At least two values are required to calculate standard deviation.")
    
    n = float(len(values))
    m = sum(values, 0.0) / n
    
    variance_sum = sum((x - m) ** 2 for x in values)
    variance = variance_sum / (n - 1)
    
    std_dev = calculate_std_dev(values)
    
    return mean(m), std_dev

def main():
    """Main execution block."""
    args = parse_arguments()

    # If no arguments were passed via CLI, use the hard-coded sample values.
    if not args.volumes:
        sample_volumes = [10, 20, 30, 40, 50]
        volumes_to_process = sample_volumes
    else:
        # Ensure we have at least one value even if the user passed an empty list (though argparse usually handles this strictly)
        volumes_to_process = args.volumes

    try:
        avg_volume, std_vol = calculate_statistics(volumes_to_process)
        
        print(f"Arithmetic Mean: {avg_volume}")
        print(f"Standard Deviation: {std_vol:.2f}")
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()