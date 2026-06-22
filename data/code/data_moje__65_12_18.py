FOOT_TO_INCH_RATIO = 12.0

def feet_to_inches(feet):
    return feet * FOOT_TO_INCH_RATIO

if __name__ == '__main__':
    feet_value = 5
    result = feet_to_inches(feet_value)
    print(result)