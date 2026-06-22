def cubic_centimeters_to_cubic_inches(cc):
    cubic_inch = 0.0610237440947
    return cc * cubic_inch

if __name__ == '__main__':
    sample_values = [100, 500, 1000]
    for value in sample_values:
        print(f"{value} cubic centimeters is {cubic_centimeters_to_cubic_inches(value)} cubic inches")