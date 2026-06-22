INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    sample_feet = 5
    result = feet_to_inches(sample_feet)
    print(result)