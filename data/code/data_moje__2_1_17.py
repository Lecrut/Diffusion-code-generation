def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10.5, 15.3, 8.7, 22.1, 18.4]
    result = calculate_average_volume(sample_volumes)
    print(result)