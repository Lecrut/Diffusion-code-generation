def calculate_average_volume(volumes):
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    volumes = [100, 200, 300, 400, 500]
    result = calculate_average_volume(volumes)
    print(result)