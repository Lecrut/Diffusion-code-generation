import sys

def calculate_volume_stats(measurements):
    """
    Calculates total and average volume from a list of measurements.
    
    Args:
        measurements (list): A list of numerical values representing volumes.
        
    Returns:
        dict: Contains 'total' and 'average'.
    """
    if not measurements:
        return {'total': 0, 'average': 0}
    
    total = sum(measurements)
    average = total / len(measurements)
    
    return {
        'total': round(total, 2),
        'average': round(average, 2)
    }

def get_sample_data():
    """
    Returns hard-coded sample volume measurements for testing without user input.
    Includes three values: 10.5, 23.4, and 7.8.
    
    Returns:
        list: List of float values representing volumes in liters.
    """
    return [10.5, 23.4, 7.8]

if __name__ == '__main__':
    # Sample data to run without any user interaction or network access
    sample_measurements = get_sample_data()
    
    print("Sample Volume Measurements (Liters):")
    for i, val in enumerate(sample_measurements, 1):
        print(f"Measurement {i}: {val} L")
    
    results = calculate_volume_stats(sample_measurements)
    
    print("\nCalculated Statistics:")
    print(f"Total Volume: {results['total']} Liters")
    print(f"Average Volume: {results['average']} Liters")