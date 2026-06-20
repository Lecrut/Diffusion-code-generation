def calculate_average_volume(volumes):
    if not volumes:
        return 0.0
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [100.0, 200.0, 300.0, 400.0, 500.0]
    result = calculate_average_volume(sample_volumes)
    print(result)