def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"

if __name__ == '__main__':
    volume_a = 100.456
    volume_b = 78.912
    result = calculate_absolute_difference(volume_a, volume_b)
    print(result)