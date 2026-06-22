def calculate_absolute_difference(volume1, volume2):
    return round(abs(volume1 - volume2), 2)

if __name__ == '__main__':
    sample_volume1 = 50.789
    sample_volume2 = 34.567
    result = calculate_absolute_difference(sample_volume1, sample_volume2)
    print(result)