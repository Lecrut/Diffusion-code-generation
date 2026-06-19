def inches_to_centimeters(length_in_inches):
    return length_in_inches * 2.54

if __name__ == '__main__':
    sample_inches = [1, 10, 0.5]
    for val in sample_inches:
        result = inches_to_centimeters(val)
        print(result)