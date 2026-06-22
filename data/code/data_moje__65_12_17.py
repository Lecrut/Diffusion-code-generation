FOOT_TO_INCH_RATIO = 12

def convert_feet_to_inches(feet):
    return feet * FOOT_TO_INCH_RATIO

if __name__ == '__main__':
    sample_feet = 5
    result = convert_feet_to_inches(sample_feet)
    print(result)