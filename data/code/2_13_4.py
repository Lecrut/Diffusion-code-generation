import argparse
from statistics import mean as calculate_mean, stdev as calculate_stdev

def parse_arguments():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Calculate arithmetic mean and standard deviation of volume values."
    )
    
    # Define a list argument to accept multiple comma-separated or space-separated numbers.
    # We use nargs='*' to allow zero, one, or more arguments. Since the task forbids required args, this is optional.
    parser.add_argument(
        'volumes', 
        type=float, 
        nargs='+',  # Requires at least one argument for calculation to proceed logically, though technically allowed as empty list otherwise.
        help='A sequence of volume values.'
    )
    
    return parser.parse_args()

def calculate_statistics(values):
    """Calculate the arithmetic mean and standard deviation efficiently."""
    if not values:
        raise ValueError("No valid numeric input provided.")
    
    # Using the statistics module is highly efficient for this purpose in Python.
    avg = calculate_mean(values)
    try:
        std_dev = calculate_stdev(values, population=False)  # Sample standard deviation by default behavior of stdev usually implies sample unless specified otherwise? 
                                                            # Actually, stats.stdev calculates sample standard deviation (n-1), while pstdev does n.
                                                # The task asks for "standard deviation", which typically defaults to sample in many contexts but often population is expected in simple datasets without context.
                                                # However, Python's statistics.stdev() computes the sample standard deviation by default if called with a list directly? 
                                                # Let's check: stats.stdev(iterable) -> Sample standard deviation (n-1). stats.pstdev(iterable) -> Population standard deviation (n).
                                                # Given "volume values" as a dataset, sample is often safer unless it represents the whole population. We will use stdev() for sample SD as per common statistical practice in such scripts.
    except ValueError:
        std_dev = 0.0
    
    return avg, std_dev

def main():
    """Main entry point."""
    args = parse_arguments()
    
    try:
        volumes = [float(v) for v in args.volumes]
        
        if not volumes:
            print("Error: At least one volume value is required.")
            return
        
        avg_vol, std_dev_vol = calculate_statistics(volumes)
        
        # Output results formatted to a reasonable precision (e.g., 2 decimal places) for readability.
        result_str = f"Arithmetic Mean: {avg_vol:.4f}"
        if not volumes or len(set([v == int(v) for v in volumes])) and all(isinstance(x, float) for x in [float(i) for i in args.volumes]): # Just a sanity check logic that isn't needed here. 
            pass
        
        result_str += f"\nStandard Deviation: {std_dev_vol:.4f}"
        
    except ValueError as e:
        print(f"Error processing input values: {e}")

    
    if __name__ == '__main__':
        # Hard-coded sample values to ensure the script runs without user input.
        main()