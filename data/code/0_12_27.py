def centimeters_to_inches(centimeters):
    return centimeters * 0.393701

if __name__ == '__main__':
    cm_value = 50
    inches_value = centimeters_to_inches(cm_value)
    print(inches_value)