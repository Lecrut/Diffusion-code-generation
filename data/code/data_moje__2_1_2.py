def calculate_average_volume(volumes):
    if not volumes:
        return 0.0
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10.5, 20.0, 15.3, 18.7, 22.5]
    result = calculate_average_volume(sample_volumes)
    print(result)