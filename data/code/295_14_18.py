def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm * 0.393701

if __name__ == '__main__':
    print(f"10 inches to cm: {inches_to_cm(10)}")
    print(f"25.4 cm to inches: {cm_to_inches(25.4)}")