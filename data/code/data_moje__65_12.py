INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    feet_value = 5
    inches_value = feet_to_inches(feet_value)
    print(inches_value)