def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm * 0.393701

if __name__ == '__main__':
    inches_value = 10.0
    cm_value = 25.4
    
    print(f"{inches_value} inches is {inches_to_cm(inches_value)} cm")
    print(f"{cm_value} cm is {cm_to_inches(cm_value)} inches")