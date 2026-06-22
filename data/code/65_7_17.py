def feet_to_inches(feet):
    return feet * 36 if isinstance(feet, (int, float)) else float(feet) * 36

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(3.5))
    print(feet_to_inches(0))
    print(feet_to_inches(-2))
    print(feet_to_inches("10"))