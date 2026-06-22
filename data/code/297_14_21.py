conversion_factor = 2.54

def inches_to_cm(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Input must be a number")
    return inches * conversion_factor

def cm_to_inches(cm):
    if not isinstance(cm, (int, float)):
        raise ValueError("Input must be a number")
    return cm / conversion_factor

if __name__ == '__main__':
    print(inches_to_cm(1))
    print(inches_to_cm(0.5))
    print(cm_to_inches(2.54))
    print(cm_to_inches(12.7))