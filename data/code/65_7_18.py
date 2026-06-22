def feet_to_inches(feet):
    return feet * 36 if isinstance(feet, (int, float)) and feet >= 0 else None

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(0))
    print(feet_to_inches(1.5))
    print(feet_to_inches(-1))
    print(feet_to_inches("abc"))