CONVERSION_FACTOR = 12

def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_inputs = [0, 1.5, 10, 3.25]
    for value in sample_inputs:
        inches = feet_to_inches(value)
        print(f"{value} feet is {inches} inches")