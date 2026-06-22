VOLUME_THRESHOLD = 0

def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    if any(volume < VOLUME_THRESHOLD for volume in volumes):
        raise ValueError("Volumes must be non-negative.")
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [20, 30, 40, 50, 60]
    try:
        average_volume = calculate_average_volume(sample_volumes)
        print(average_volume)
    except ValueError as e:
        print(e)