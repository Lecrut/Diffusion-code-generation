def calculate_average_volume(volumes):
    if not volumes:
        return 0
    return sum(volumes) / len(volumes)
if __name__ == '__main__':
    sample_volumes = [10.5, 20.0, 15.5, 30.0, 14.0]
    average = calculate_average_volume(sample_volumes)
    print(average)