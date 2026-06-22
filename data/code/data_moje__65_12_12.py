FEET_TO_INCHES_RATIO = 12

def feet_to_inches(feet):
    return feet * FEET_TO_INCHES_RATIO

if __name__ == '__main__':
    hard_coded_feet = 5.5
    result = feet_to_inches(hard_coded_feet)
    print(result)