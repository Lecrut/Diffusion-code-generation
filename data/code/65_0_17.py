CONVERSION_FACTOR = 12

def feet_to_inches(feet):
    inches = feet * CONVERSION_FACTOR
    return inches

if __name__ == '__main__':
    sample_value = 7.25
    converted_inches = feet_to_inches(sample_value)
    print(converted_inches)