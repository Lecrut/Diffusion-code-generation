def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)
if __name__ == '__main__':
    sample_volumes = [10.5, 20.0, 15.5, 25.0, 18.0]
    average = calculate_average_volume(sample_volumes)
    print(average)