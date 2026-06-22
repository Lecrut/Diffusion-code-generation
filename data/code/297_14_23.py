def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

if __name__ == '__main__':
    print(f"1 inch is {inches_to_cm(1)} cm")
    print(f"1 cm is {cm_to_inches(1)} inches")