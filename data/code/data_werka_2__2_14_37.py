def convert_volume(cc):
    conversion_factor = 0.0610237440947
    cubic_inches = cc * conversion_factor
    return cubic_inches

if __name__ == '__main__':
    sample_values = [300, 800, 1200]
    for value in sample_values:
        converted_value = convert_volume(value)
        print(f'{value} cubic centimeters is {converted_value:.6f} cubic inches')