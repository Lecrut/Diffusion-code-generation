def cm_to_inches(centimeters):
    return centimeters * 0.393701

if __name__ == '__main__':
    sample_value = 50
    inches = cm_to_inches(sample_value)
    print(inches)