import argparse
from statistics import mean, stdev

def parse_volume_list():
    """Parses a list of volume values from command-line arguments."""
    parser = argparse.ArgumentParser(description="Calculate arithmetic mean and standard deviation of volumes.")
    
    # Using optional argument to avoid requiring input via stdin or prompts
    args = parser.parse_args()

    if not hasattr(args, 'volumes') or len(args.volumes) == 0:
        return None
    
    try:
        values = [float(v) for v in args.volumes]
        # Ensure at least two numbers exist to calculate standard deviation
        if len(values) < 2:
            raise ValueError("At least two volume values are required.")
        
        avg_volume = mean(values)
        std_deviation = stdev(values)

        return {
            'values': values,
            'mean': avg_volume,
            'std_deviation': std_deviation
        }
    except (ValueError, TypeError):
        raise ValueError("All volume values must be valid numbers.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    # Simulating command-line arguments for demonstration purposes within this block.
    sample_volumes = [10, 25, 30, 45, 60]

    result_data = parse_volume_list()
    
    if result_data is None:
        print("Error: No volume values provided.")
    else:
        volumes = result_data['values']
        avg_vol = result_data['mean']
        std_dev = result_data['std_deviation']

        # Output results efficiently without interactive prompts.
        print(f"Volume Values: {volumes}")
        print(f"Arithmetic Mean: {avg_vol:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")