VOLUME_CONVERSION_FACTOR = 0.0610237440947

def convert_volume(cc):
    return cc * VOLUME_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_values = [300, 600, 900]
    for value in sample_values:
        result = convert_volume(value)
        print(f'{value} cubic centimeters is {result:.4f} cubic inches')