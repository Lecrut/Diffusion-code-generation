def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError('Input must be an integer or float.')
    return feet * 12
if __name__ == '__main__':
    sample_feet = [0, 1, 5.5, 10, -3]
    for feet in sample_feet:
        print(feet_to_inches(feet))