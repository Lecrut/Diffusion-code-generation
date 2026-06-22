def cubic_centimeters_to_cubic_inches(cc):
    conversion_factor = 1 / 16.387064
    return cc * conversion_factor
if __name__ == '__main__':
    sample_values = [100, 500, 1000]
    for value in sample_values:
        result = cubic_centimeters_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {result:.4f} cubic inches')