def calculate_total_volume(volumes):
    total = 0
    for vol in volumes.values():
        total += vol
    return total

if __name__ == '__main__':
    sample_data = {
        'cube': 8,
        'sphere': 4.18879,
        'cylinder': 12.56637
    }
    result = calculate_total_volume(sample_data)
    print(result)