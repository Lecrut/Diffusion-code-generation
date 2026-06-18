import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return 0, 0
    
    total = sum(measurements)
    average = statistics.mean(measurements)
    
    return total, average

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed)
    sample_measurements = [10.5, 20.3, 15.7, 8.9]
    
    # Calculate results using the helper function
    total_volume, avg_volume = calculate_volume_stats(sample_measurements)
    
    # Display output to console (no interactive prompts used)
    print(f"Total Volume: {total_volume}")
    print(f"Average Volume: {avg_volume:.2f}")