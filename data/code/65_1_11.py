INCHES_PER_FOOT = 12
def calculate_inches(feet):
    if not isinstance(feet, (int, float)):
        return None
    if feet < 0:
        return None
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    sample_feet = 10
    inches = calculate_inches(sample_feet)
    print(inches)