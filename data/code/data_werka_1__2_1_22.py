def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10, 20, 30, 40, 50]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)