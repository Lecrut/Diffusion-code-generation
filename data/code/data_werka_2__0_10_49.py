def cm_to_inches(cm):
    return cm / 2.54

if __name__ == '__main__':
    cm_value = 50
    inches_value = cm_to_inches(cm_value)
    print(inches_value)