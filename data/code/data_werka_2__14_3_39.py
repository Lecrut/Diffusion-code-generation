def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"

if __name__ == '__main__':
    first_volume = 75.345
    second_volume = 68.901
    formatted_difference = calculate_absolute_difference(first_volume, second_volume)
    print(formatted_difference)