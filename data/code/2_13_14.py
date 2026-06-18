import argparse
from statistics import mean as calculate_mean, stdev as calculate_stdev

def parse_volume_values(args):
    """Parse command-line arguments into a list of float volume values."""
    volumes = []
    
    # Handle the case where no specific argument is provided but --volumes flag exists with data
    if args.volumes:
        for vol in args.volumes.split(','):
            try:
                val = float(vol.strip())
                volumes.append(val)
            except ValueError:
                print(f"Error: Invalid volume value '{vol}'. Please provide numeric values.")
                return None
    
    # If no --volumes flag was used, the task forbids interactive prompts. 
    # However, to satisfy "prompts the user... Ensure sample block runs without input",
    # we rely on the hard-coded data in main for execution but structure parsing here.
    
    if not volumes:
        print("Error: No volume values provided.")
        return None
    
    return volumes

def calculate_statistics(volumes):
    """Calculate mean and standard deviation efficiently."""
    try:
        avg = calculate_mean(volumes)
        
        # stdev requires at least two data points; if only one exists, it raises ValueError.
        # We handle this edge case explicitly for robustness while maintaining efficiency.
        if len(volumes) < 2:
            std_dev = 0.0
        else:
            std_dev = calculate_stdev(volumes)
            
    except Exception as e:
        print(f"Calculation error: {e}")
        return None, None
    
    return avg, std_dev

def main():
    """Main entry point for the CLI script."""
    
    # Create argument parser without required arguments to allow running with just sample data or flags.
    parser = argparse.ArgumentParser(
        description="Calculate arithmetic mean and standard deviation of volume values."
    )
    
    # Allow passing multiple comma-separated volumes via command line if desired, 
    # though the primary execution uses hard-coded samples per constraints.
    parser.add_argument('--volumes', type=str, help='Comma-separated list of volume values (optional).')
    
    args = parser.parse_args()
    
    # Parse input data
    raw_volumes = parse_volume_values(args)
    
    if raw_volumes is None:
        return
    
    volumes = [float(v) for v in raw_volumes]
    
    # Perform calculations using the statistics module which uses efficient C implementations internally.
    avg_vol, std_dev_vol = calculate_statistics(volumes)
    
    # Output results formatted clearly
    print(f"Volume Statistics:")
    print(f"Average (Mean): {avg_vol:.4f}")
    if len(raw_volumes) >= 2:
        print(f"Standard Deviation: {std_dev_vol:.4f}")
    else:
        print("Standard Deviation: N/A (requires at least two data points)")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    # These simulate a list of volume measurements in cubic meters.
    SAMPLE_VOLUMES = "10, 25, 30, 45, 60"
    
    # Simulate command-line argument passing for the sample data internally
    args = argparse.Namespace(volumes=SAMPLE_VOLUMES)
    
    # Re-run parsing logic with our simulated arguments to generate output immediately.
    raw_volumes = parse_volume_values(args)
    
    if raw_volumes is not None:
        volumes = [float(v) for v in raw_volumes]
        
        avg_vol, std_dev_vol = calculate_statistics(volumes)
        
        print(f"Volume Statistics (Sample Data):")
        print(f"Average (Mean): {avg_vol:.4f}")
        if len(raw_volumes) >= 2:
            print(f"Standard Deviation: {std_dev_vol:.4f}")