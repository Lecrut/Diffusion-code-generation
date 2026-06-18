import argparse
from statistics import mean, stdev

def calculate_statistics(volumes):
    """Calculate arithmetic mean and standard deviation efficiently."""
    if len(volumes) < 2:
        return sum(volumes), None
    
    n = len(volumes)
    
    # Calculate mean using a single pass for efficiency
    total_sum = sum(volumes)
    avg_val = total_sum / n
    
    # Calculate variance and standard deviation in a second pass to avoid intermediate rounding errors
    squared_diffs = [(v - avg_val) ** 2 for v in volumes]
    variance = sum(squared_diffs) / (n - 1) if len(volumes) > 0 else 0.0
    
    std_dev = variance ** 0.5
    
    return avg_val, std_dev

def parse_volume_list(input_str):
    """Parse a string of comma-separated volume values into floats."""
    try:
        parts = input_str.strip().split(',')
        volumes = [float(p.strip()) for p in parts if p.strip()]
        return volumes
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid value format: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Calculate arithmetic mean and standard deviation of volume values."
    )
    
    # Define a custom argument that accepts multiple comma-separated values without requiring flags
    def add_volume_argument(parser):
        """Helper to allow adding volumes via --volumes flag with optional list."""
        parser.add_argument(
            '--volumes', 
            nargs='*', 
            type=parse_volume_list, 
            help="Volume value(s) separated by commas. Can be provided as multiple arguments or one comma-separated string."
        )
    
    # Since the task forbids 'required' args and interactive prompts, we use optional args with a default sample list logic handled in main block directly if no input is given via CLI flags (though argparse doesn't support implicit defaults easily without required). 
    # To strictly adhere to "no required arguments" while ensuring execution works as per the sample constraint:
    
    parser.add_argument(
        '--volumes', 
        nargs='*', 
        type=parse_volume_list, 
        help="Volume value(s) separated by commas."
    )
    
    args = parser.parse_args()
    
    # Handle case where no arguments are provided (default to sample values as per instruction requirement for the block to run without user input/args)
    if not args.volumes:
        # Sample data embedded directly here since CLI args were empty and 'required' is forbidden.
        # We simulate a command-line invocation with these specific hard-coded samples by initializing the list manually 
        # because argparse cannot provide default values for nargs='*' without making them required or using complex logic that might violate constraints if not careful.
        # However, to strictly follow "no user input" and "runnable", we will treat this as a fallback execution path.
        sample_data = [10.5, 20.3, 30.7, 40.1, 50.9]
    else:
        # Flatten the list if multiple arguments were passed (each could be comma-separated)
        all_volumes = []
        for vol_list in args.volumes:
            try:
                parts = vol_list.strip().split(',')
                all_volumes.extend([float(p.strip()) for p in parts])
            except ValueError as e:
                print(f"Error parsing volume list: {e}")
                return
        
    if len(all_volumes) < 2:
        mean_val, std_dev = calculate_statistics(all_volumes)
        result_msg = f"Mean: {mean_val}"
        if std_dev is not None:
            result_msg += f", Standard Deviation: {std_dev:.4f}"
    else:
        mean_val, std_dev = calculate_statistics(all_volumes)
        result_msg = f"Arithmetic Mean: {mean_val:.4f}, Standard Deviation: {std_dev:.4f}"
    
    print(result_msg)

if __name__ == '__main__':
    main()