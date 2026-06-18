import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return 0, None
    
    total = sum(measurements)
    average = total / len(measurements)
    
    return total, average

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments needed)
    sample_measurements = [10.5, 23.7, 45.2, 60.8]
    
    print("Processing volume measurements...")
    total_volume, average_volume = calculate_volume_stats(sample_measurements)
    
    if average_volume is not None:
        print(f"Total Volume: {total_volume}")
        print(f"Average Volume: {average_volume:.2f}")
    else:
        print("No valid measurements provided.")