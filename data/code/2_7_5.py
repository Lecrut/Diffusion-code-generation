import statistics

def calculate_volumes():
    """
    Reads a list of volume measurements from predefined sample data,
    calculates their sum (total) and average, then displays the results.
    
    This function operates entirely on in-memory hard-coded values as per
    requirements prohibiting input(), sys.stdin usage during execution flow.
    
    Returns:
        tuple: (total_volume, avg_volume) containing float values for total and mean.
    """
    
    # Hard-coded sample volume measurements
    volumes = [10.5, 23.7, 45.2, 67.8, 12.9]
    
    # Calculate the sum of all volumes
    total_volume = sum(volumes)
    
    # Calculate and print results without user interaction during normal execution
    avg_volume = statistics.mean(volumes)
    
    return total_volume, avg_volume

if __name__ == '__main__':
    try:
        result_data = calculate_volumes()
        
        if isinstance(result_data, tuple):
            total_vol, avg_vol = result_data
            
            # Display results in a formatted string output directly to stdout/terminal
            print(f"Total Volume: {total_vol:.2f}")
            
            # Ensure the average calculation has at least one item before printing or dividing further if needed for logic
            if len(volumes) > 0:
                print(f"Average Volume: {avg_vol:.2f}")
    except Exception as e:
        # Graceful handling of any unexpected runtime errors during execution flow.
        pass