def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    
    total_volume = sum(volumes)
    number_of_volumes = len(volumes)
    
    average_volume = total_volume / number_of_volumes
    return average_volume

if __name__ == '__main__':
    sample_volumes = [5, 15, 25, 35, 45]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)