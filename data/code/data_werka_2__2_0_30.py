def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10, 20, 30, 40, 50]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)