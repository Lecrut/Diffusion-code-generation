def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"

if __name__ == '__main__':
    sample_volume1 = 15.789
    sample_volume2 = 10.345
    result = calculate_absolute_difference(sample_volume1, sample_volume2)
    print(result)