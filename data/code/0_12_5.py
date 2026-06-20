def convert_cm_to_inches(cm: float) -> float:
    return cm / 2.54

if __name__ == '__main__':
    result = convert_cm_to_inches(50)
    print(result)