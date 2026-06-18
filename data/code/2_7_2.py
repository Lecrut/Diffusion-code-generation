import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return 0, None
    
    total = sum(measurements)
    average = statistics.mean(measurements)
    
    return total, average

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments used)
    sample_measurements = [10.5, 20.3, 15.7, 8.9, 12.1]
    
    total_volume, average_volume = calculate_volume_stats(sample_measurements)
    
    print(f"Total Volume: {total_volume}")
    if average_volume is not None:
        print(f"Average Volume: {average_volume:.2f}")