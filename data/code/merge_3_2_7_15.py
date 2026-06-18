import statistics

def calculate_volumes():
    """
    Calculates total and average volume from a list of measurements.
    
    Returns:
        tuple: (total_volume, average_volume)
    """
    volumes = [10, 25, 30]
    
    if not volumes:
        return None, None
    
    total_volume = sum(volumes)
    average_volume = statistics.mean(volumes)
    
    return total_volume, average_volume

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or args)
    result_total, result_average = calculate_volumes()
    
    if result_total is None:
        print("No volume data provided.")
    else:
        print(f"Total Volume: {result_total}")
        print(f"Average Volume: {result_average:.2f}")