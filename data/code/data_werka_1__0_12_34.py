def centimeters_to_inches(cm):
    return cm * 0.393701

if __name__ == '__main__':
    sample_cm = 50
    inches = centimeters_to_inches(sample_cm)
    print(inches)