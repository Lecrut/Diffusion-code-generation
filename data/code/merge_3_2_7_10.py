import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return 0, None
    
    total = sum(measurements)
    try:
        avg = statistics.mean(measurements)
    except ValueError:
        # Fallback for empty sequence or non-numeric data (though input validation is assumed here)
        avg = None
        
    return total, avg

def main():
    """Main function to run the application with hard-coded sample values."""
    
    # Hard-coded sample volume measurements in liters
    sample_measurements = [2.5, 3.0, 4.1, 2.8, 3.5]
    
    print("Volume Measurement Calculator")
    print("-" * 30)
    
    total_volume, average_volume = calculate_volume_stats(sample_measurements)
    
    if sample_measurements:
        print(f"\nTotal Volume: {total_volume} liters")
        
        # Only display average if it's a valid number (not None due to empty list check above)
        if isinstance(average_volume, float):
            print(f"Average Volume: {average_volume:.2f} liters")

if __name__ == '__main__':
    main()