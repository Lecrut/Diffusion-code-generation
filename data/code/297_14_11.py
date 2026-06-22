def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54
if __name__ == '__main__':
    print(inches_to_cm(1))
    print(inches_to_cm(0.5))
    print(cm_to_inches(2.54))
    print(cm_to_inches(12.7))