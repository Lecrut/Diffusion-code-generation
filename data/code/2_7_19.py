import math

def calculate_volumes():
    """
    Calculates total and average volume from a list of measurements.
    
    Returns:
        tuple: (total_volume, average_volume) rounded to two decimal places.
    """
    volumes = [10.5, 25.3, 7.8, 40.2]

    # Calculate total volume
    total_volume = sum(volumes)

    # Calculate average volume and handle empty list edge case (though sample isn't empty here)
    if len(volumes) > 0:
        average_volume = total_volume / len(volumes)
    else:
        average_volume = 0.0

    return round(total_volume, 2), round(average_volume, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or args used in logic execution flow for interaction)
    total_vol, avg_vol = calculate_volumes()

    print(f"Total Volume: {total_vol}")
    print(f"Average Volume: {avg_vol}")