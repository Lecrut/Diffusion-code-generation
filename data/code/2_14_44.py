def cubic_centimeters_to_cubic_inches(cc):
    return cc * 0.0610237

if __name__ == '__main__':
    sample_values = [100, 500, 1000]
    for value in sample_values:
        result = cubic_centimeters_to_cubic_inches(value)
        print(f"{value} cubic centimeters is {result} cubic inches")