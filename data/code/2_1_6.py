def calculate_average_volume(volumes):
    if not volumes:
        return 0.0
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 15.7, 25.1, 30.4]
    result = calculate_average_volume(sample_volumes)
    print(result)