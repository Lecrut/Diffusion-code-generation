def calculate_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"
if __name__ == '__main__':
    v1 = 10.567
    v2 = 12.345
    result = calculate_difference(v1, v2)
    print(result)