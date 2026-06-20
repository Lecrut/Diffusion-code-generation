def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [100, 150, 200, 250, 300]
    result = calculate_average_volume(sample_volumes)
    print(result)