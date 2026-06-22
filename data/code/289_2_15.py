def inches_to_millimeters(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Invalid input type. Use integer or float.')
    return value * 25.4
if __name__ == '__main__':
    sample_value = 10
    result = inches_to_millimeters(sample_value)
    print(f'{sample_value} inches is {result} millimeters')