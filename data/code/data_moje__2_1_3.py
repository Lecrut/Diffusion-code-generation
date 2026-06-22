def calculate_average_volume(measurements):
    if not measurements:
        return 0.0
    return sum(measurements) / len(measurements)

if __name__ == '__main__':
    sample_volumes = [10.5, 20.0, 15.5, 30.0, 25.0]
    result = calculate_average_volume(sample_volumes)
    print(result)