def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    constant = 12
    return feet * constant

if __name__ == '__main__':
    sample_feet = 8.5
    result = feet_to_inches(sample_feet)
    print(result)