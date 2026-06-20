def calculate_average_volume(volumes):
    if not volumes:
        return 0.0
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    volumes = [10.5, 20.3, 15.7, 30.0, 25.2]
    result = calculate_average_volume(volumes)
    print(result)