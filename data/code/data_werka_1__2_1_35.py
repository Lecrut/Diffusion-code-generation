def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 30.7, 40.2, 50.9]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)