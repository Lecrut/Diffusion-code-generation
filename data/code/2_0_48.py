def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("The list of volumes cannot be empty.")
    total = sum(volumes)
    count = len(volumes)
    average = total / count
    return average

if __name__ == '__main__':
    sample_volumes = [50, 60, 70, 80, 90]
    try:
        result = calculate_average_volume(sample_volumes)
        print(result)
    except ValueError as e:
        print(e)