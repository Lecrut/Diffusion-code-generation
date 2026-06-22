def cubic_centimeters_to_cubic_inches(cc):
    cubic_inch = 0.0610237440947
    return cc * cubic_inch

if __name__ == '__main__':
    sample_values = [100, 500, 1000]
    for value in sample_values:
        result = cubic_centimeters_to_cubic_inches(value)
        print(f"{value} cubic centimeters is {result} cubic inches")