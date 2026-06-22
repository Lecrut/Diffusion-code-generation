def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes) if volumes else 0

if __name__ == '__main__':
    sample_volumes = [100, 200, 300, 400, 500]
    average_volume = calculate_average_volume(sample_volumes)
    print(average_volume)