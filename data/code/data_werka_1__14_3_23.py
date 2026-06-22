def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"

if __name__ == '__main__':
    volume_a = 105.789
    volume_b = 100.456
    result = calculate_absolute_difference(volume_a, volume_b)
    print(result)