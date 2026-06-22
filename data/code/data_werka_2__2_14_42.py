def cubic_centimeters_to_cubic_inches(cc):
    conversion_factor = 0.0610237440947
    return cc * conversion_factor

if __name__ == '__main__':
    sample_values = [50, 200, 800]
    for value in sample_values:
        result = cubic_centimeters_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')