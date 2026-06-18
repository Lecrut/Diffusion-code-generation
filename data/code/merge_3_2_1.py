def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)
if __name__ == '__main__':
    sample_volumes = [10.5, 22.0, 15.75, 30.25]
    average = calculate_average_volume(sample_volumes)
    print(average)