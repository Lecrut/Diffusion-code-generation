import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return None, None
    
    total = sum(measurements)
    avg = statistics.mean(measurements)
    
    return total, avg

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input or args needed)
    sample_measurements = [10.5, 23.7, 45.2, 60.8]
    
    print("Calculating volume statistics for the following measurements:")
    print(f"Measurements: {sample_measurements}")
    
    total_volume, average_volume = calculate_volume_stats(sample_measurements)
    
    if total_volume is not None and average_volume is not None:
        print(f"\nTotal Volume: {total_volume:.2f}")
        print(f"Average Volume: {average_volume:.2f}")
    else:
        print("No valid measurements provided.")