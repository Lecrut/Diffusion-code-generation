def feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError('feet must be a numeric type (int or float)')
    if feet < 0:
        raise ValueError('feet must be a non-negative value')
    return feet * 12
if __name__ == '__main__':
    sample_feet_values = [0, 1, 5.5, 10, 100]
    for feet in sample_feet_values:
        inches = feet_to_inches(feet)
        print(f'{feet} feet = {inches} inches')