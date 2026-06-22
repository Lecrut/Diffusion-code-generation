CONVERSION_FACTOR = 1 / 2.54

def convert_cm_to_inches(cm):
    return cm * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_cm = 50
    inches = convert_cm_to_inches(sample_cm)
    print(inches)