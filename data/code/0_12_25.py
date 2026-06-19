def convert_cm_to_inches(cm):
    return cm * 0.393701

if __name__ == '__main__':
    cm_value = 50
    inches_value = convert_cm_to_inches(cm_value)
    print(inches_value)