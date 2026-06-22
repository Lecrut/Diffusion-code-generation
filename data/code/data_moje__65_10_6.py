def convert_feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError('Input must be a number.')
    if feet < 0:
        raise ValueError('Input must be non-negative.')
    return feet * 12
if __name__ == '__main__':
    sample_feet_values = [0, 1, 5.5, 10, 100.25]
    for feet in sample_feet_values:
        inches = convert_feet_to_inches(feet)
        print(f'{feet} feet is equal to {inches} inches.')