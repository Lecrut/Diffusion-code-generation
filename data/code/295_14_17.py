def inches_to_cm(inches):
    cm_per_inch = 2.54
    return inches * cm_per_inch

def cm_to_inches(cm):
    inches_per_cm = 0.393701
    return cm * inches_per_cm

if __name__ == '__main__':
    sample_inches = 5.0
    sample_cm = 12.7

    converted_cm = inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is {converted_cm:.2f} cm")

    converted_inches = cm_to_inches(sample_cm)
    print(f"{sample_cm} cm is {converted_inches:.2f} inches")