def calculate_average_volume(volumes):
    if not volumes:
        raise ValueError("List of volumes must not be empty")
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [10.5, 12.3, 15.8, 8.2, 11.1]
    average = calculate_average_volume(sample_volumes)
    print(average)