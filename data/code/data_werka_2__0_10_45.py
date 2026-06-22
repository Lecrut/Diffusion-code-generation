def cm_to_inches(centimeters):
    return centimeters * 0.393701

if __name__ == '__main__':
    sample_cm = 60
    inches = cm_to_inches(sample_cm)
    print(inches)