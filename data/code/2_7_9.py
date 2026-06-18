import statistics

def calculate_volumes():
    """
    Calculates total and average volume from a list of measurements.
    
    Returns:
        tuple: (total_volume, average_volume)
    """
    volumes = [10, 25, 30]  # Hard-coded sample values
    
    if not volumes:
        return None, None

    total_volume = sum(volumes)
    average_volume = statistics.mean(volumes)
    
    return total_volume, average_volume

if __name__ == '__main__':
    result_total, result_average = calculate_volumes()
    
    print("Total Volume:", result_total)
    if result_average is not None:
        print("Average Volume:", result_average)