def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = [0, 1, 2.5, 10, 100]
    for val in sample_inches:
        print(inches_to_centimeters(val))