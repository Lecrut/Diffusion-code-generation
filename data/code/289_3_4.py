def feet_to_micrometers(feet):
    if not isinstance(feet, (int, float)) or feet < 0:
        raise ValueError("Input must be a non-negative number")
    return feet * 304800

if __name__ == '__main__':
    print(feet_to_micrometers(1))
    print(feet_to_micrometers(5))
    print(feet_to_micrometers(10))