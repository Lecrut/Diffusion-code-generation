def convert_cubic_centimeters_to_cubic_inches(cubic_centimeters):
    conversion_factor = 0.0610237440947
    cubic_inches = cubic_centimeters * conversion_factor
    return cubic_inches

if __name__ == '__main__':
    sample_values = [250, 750, 1500]
    for value in sample_values:
        converted_value = convert_cubic_centimeters_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {converted_value:.6f} cubic inches')