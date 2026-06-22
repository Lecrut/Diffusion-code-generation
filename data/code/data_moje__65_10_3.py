def feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError('Input must be a number.')
    if feet < 0:
        raise ValueError('Distance cannot be negative.')
    return feet * 12
if __name__ == '__main__':
    sample_feet = [1, 5.5, 0, 10]
    for f in sample_feet:
        print(feet_to_inches(f))