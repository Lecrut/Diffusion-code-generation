import statistics as stats

def calculate_volume_stats(volumes):
    """Calculate total and average volume from a list of measurements."""
    if not volumes:
        return 0, None
    
    total = sum(volumes)
    avg = total / len(volumes)
    
    # Ensure the result is rounded to avoid floating point precision issues in display
    avg_rounded = round(avg, 2)
    
    return total, avg_rounded

if __name__ == '__main__':
    # Hard-coded sample volume measurements (in liters)
    samples = [5.0, 10.5, 3.2, 7.8, 9.0]
    
    print("Processing volume calculations...")
    total_volume, average_volume = calculate_volume_stats(samples)
    
    if average_volume is not None:
        print(f"Total Volume: {total_volume:.1f} L")
        print(f"Average Volume: {average_volume} L")
    else:
        print("No volume data provided.")