CONVERSION_FACTOR = 0.0610237440947

def convert_volume(cc):
    if cc < 0:
        raise ValueError("Volume cannot be negative")
    return cc * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_values = [50, 200, 500]
    for value in sample_values:
        result = convert_volume(value)
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')