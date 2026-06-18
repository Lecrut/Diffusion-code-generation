import argparse
from statistics import mean as calculate_mean, stdev as calculate_stdev

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate arithmetic mean and standard deviation of volume values."
    )
    
    # Add a non-required argument for flexibility; the task forbids required args.
    # We will use this to accept multiple floats separated by spaces or newlines in one go,
    # but since we cannot call input(), argparse is used solely here as requested 
    # (though typically it's avoided if no arguments are needed).
    # To strictly adhere to "Never call... argparse required arguments", we define a non-required list.
    
    parser.add_argument(
        'volumes',
        nargs='*',  # Non-required, accepts zero or more items
        type=float,
        help="List of volume values."
    )
    
    return parser.parse_args()

def calculate_statistics(values):
    """Calculate mean and standard deviation efficiently."""
    if not values:
        raise ValueError("No valid numerical data provided.")
    
    # Using the 'statistics' module is highly efficient for these specific calculations.
    avg = calculate_mean(values)
    
    try:
        std_dev = calculate_stdev(values, population=False)  # Sample standard deviation by default in Python's statistics.stdev() if n > 1
    except ValueError as e:
        raise ValueError(f"Cannot compute standard deviation with less than two values: {e}") from e
    
    return avg, std_dev

def main():
    """Main execution block."""
    args = parse_arguments()
    
    # Convert input strings to floats if necessary (argparse handles this via type=float)
    volumes = [float(v) for v in args.volumes]
    
    try:
        average_volume, std_deviation = calculate_statistics(volumes)
        
        print(f"Arithmetic Mean: {average_volume}")
        print(f"Standard Deviation (Sample): {std_deviation:.4f}" if len(args.volumes) > 1 else "Standard Deviation (Population): N/A")
    except ValueError as ve:
        print(f"Error during calculation: {ve}", file=__import__('sys').stderr)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    # Simulating a scenario where arguments are passed directly in code logic 
    # by temporarily modifying args before execution, as argparse cannot be bypassed easily 
    # while still using it for parsing structure (as per task constraints).
    
    import sys
    
    original_argv = sys.argv[1:]  # Keep the rest of argv if any existed during module load context simulation
    
    # Inject sample values into arguments to simulate command-line input without user interaction.
    # This satisfies "hard-coded sample values" and avoids interactive prompts or stdin calls.
    sample_data = [50, 60, 70, 80, 90]
    
    sys.argv[1:] = str(sample_data).split()
    
    main()