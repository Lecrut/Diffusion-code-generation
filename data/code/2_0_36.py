def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    
    total_volume = sum(volumes)
    count_of_volumes = len(volumes)
    
    average_volume = total_volume / count_of_volumes
    
    return average_volume

if __name__ == '__main__':
    sample_volumes = [12, 24, 36, 48, 60]
    try:
        avg_vol = calculate_average_volume(sample_volumes)
        print(f"The average volume is: {avg_vol}")
    except ValueError as e:
        print(e)