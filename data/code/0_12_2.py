CONVERSION_FACTOR = 0.393701

def convert_cm_to_inches(cm):
    return cm * CONVERSION_FACTOR

if __name__ == '__main__':
    cm_input = 50
    result = convert_cm_to_inches(cm_input)
    print(result)