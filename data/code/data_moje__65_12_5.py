CONVERSION_RATIO = 12.0

def feet_to_inches(feet):
    return feet * CONVERSION_RATIO

if __name__ == '__main__':
    sample_feet = 5
    result = feet_to_inches(sample_feet)
    print(result)