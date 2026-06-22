def cm_to_inches(cm):
    if not isinstance(cm, (int, float)):
        raise ValueError("Input must be a number.")
    return cm / 2.54

if __name__ == '__main__':
    sample_cm = 50
    inches = cm_to_inches(sample_cm)
    print(inches)