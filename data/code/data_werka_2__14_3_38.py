VOLUME_PRECISION = 2

def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.{VOLUME_PRECISION}f}"

if __name__ == '__main__':
    sample_volume1 = 75.349
    sample_volume2 = 68.234
    result = calculate_absolute_difference(sample_volume1, sample_volume2)
    print(result)