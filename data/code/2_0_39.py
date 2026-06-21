def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    
    total_volume = sum(volumes)
    number_of_volumes = len(volumes)
    
    average_volume = total_volume / number_of_volumes
    return average_volume

if __name__ == '__main__':
    SAMPLE_VOLUMES = [20, 40, 60, 80, 100]
    try:
        average_volume = calculate_average_volume(SAMPLE_VOLUMES)
        print(average_volume)
    except ValueError as e:
        print(e)