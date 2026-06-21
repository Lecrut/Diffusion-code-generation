def cubic_centimeters_to_cubic_inches(cc):
    cubic_inch = cc / 16387.064
    return cubic_inch

if __name__ == '__main__':
    sample_values = [1000, 2000, 5000]
    for value in sample_values:
        result = cubic_centimeters_to_cubic_inches(value)
        print(f"{value} cubic centimeters is {result:.6f} cubic inches")