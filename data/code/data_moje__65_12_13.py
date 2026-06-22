INCHES_PER_FOOT = 12.0

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    feet_value = 5
    result = feet_to_inches(feet_value)
    print(result)