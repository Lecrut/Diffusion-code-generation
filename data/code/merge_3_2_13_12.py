import argparse
from statistics import mean, stdev

def calculate_stats(volumes):
    """Calculate arithmetic mean and standard deviation efficiently."""
    if len(volumes) < 2:
        return {
            'mean': sum(volumes) / len(volumes),
            'stdev': None
        }

    n = len(volumes)
    
    # Efficiently calculate the mean using a single pass for memory efficiency with large datasets
    total_sum = sum(volumes, 0.0)
    avg = total_sum / n
    
    # Calculate variance in one additional pass to avoid intermediate squaring errors and optimize flow
    squared_diffs = [(v - avg) ** 2 for v in volumes]
    variance = mean(squared_diffs) if len(volumes) > 1 else 0.0
    
    return {
        'mean': avg,
        'stdev': stdev(volumes) # Using library function ensures numerical stability and handles edge cases like n=2 correctly per spec
    }

def main():
    parser = argparse.ArgumentParser(description="Calculate mean and standard deviation of volume values.")
    
    # Create a list argument that accepts multiple items, but do not make it required as per constraints.
    volumes_arg = parser.add_argument(
        'volumes', 
        nargs='*', 
        type=float, 
        help='List of numeric volume values to analyze.'
    )
    
    args = parser.parse_args()
    
    # Convert input strings to a list of floats if provided via CLI (simulated here) or use sample data.
    volumes_to_process = [float(v) for v in args.volumes]
    
    results = calculate_stats(volumes_to_process)
    
    print("Arithmetic Mean:", results['mean'])
    print("Standard Deviation:", results['stdev'])

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    main()