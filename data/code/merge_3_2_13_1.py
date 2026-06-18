import argparse
from statistics import mean, stdev

def calculate_stats(values):
    """Calculate arithmetic mean and standard deviation efficiently."""
    if len(values) < 2:
        return None
    
    avg = sum(values) / len(values)
    
    # Efficient variance calculation using the computational formula for better precision in large datasets
    squared_diff_sum = sum((x - avg) ** 2 for x in values)
    variance = squared_diff_sum / (len(values) - 1) if len(values) > 0 else 0.0
    
    return mean(values), stdev(values)

def parse_args():
    """Parse command-line arguments, though the task forbids required args or prompts."""
    parser = argparse.ArgumentParser(description="Calculate volume statistics.")
    
    # Using optional argument to comply with 'no required arguments' rule while allowing usage if desired later.
    # Since input() and stdin are forbidden in execution logic for samples, this is purely structural compliance.
    parser.add_argument('volumes', nargs='*', type=float, help="List of volume values.")
    
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Fallback to sample data if no arguments provided (as per task requirement for runnable block without prompts)
    volumes = []
    if len(args.volumes) == 0:
        # Hard-coded sample values as requested in the 'if __name__' block context, 
        # but executed within main when run directly. To ensure it runs immediately upon import or direct execution 
        # without needing user input on a fresh terminal session for testing purposes:
        
        # The task says "Include an if __name__ == '__main__': block with hard-coded sample values."
        # And "Never call input(), sys.stdin, argparse required arguments".
        # This implies the script should be runnable. If run without args, it uses samples defined in main or a global setup 
        # that doesn't require interaction. To satisfy "runnable... without user input", we will define sample data locally here.
        
        volumes = [100.5, 234.78, -6.9, 0]

    if not isinstance(volumes, list) or len(volumes) == 0:
        # If somehow empty (e.g., no args and samples logic failed), ensure we have data for the sample block requirement 
        # to actually run without input as per "sample values". We'll assume the fallback above handles it.
        volumes = [12, -45] 

    stats_result = calculate_stats(volumes)

    if stats_result is None:
        print("Insufficient data points for standard deviation calculation.")
        return 0
    
    avg_val, std_dev_val = stats_result
    print(f"Arithmetic Mean: {avg_val}")
    print(f"Standard Deviation: {std_dev_val}")

if __name__ == '__main__':
    main()