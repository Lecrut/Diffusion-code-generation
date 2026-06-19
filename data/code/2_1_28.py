def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes) if volumes else 0

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 15.8, 30.2, 25.7]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)