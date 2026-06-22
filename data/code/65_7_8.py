def feet_to_inches(feet):
    return feet * 36.0 if feet else 0.0

if __name__ == '__main__':
    sample_feet = 5.5
    print(feet_to_inches(sample_feet))
    sample_feet_zero = 0
    print(feet_to_inches(sample_feet_zero))
    sample_feet_float = 10.25
    print(feet_to_inches(sample_feet_float))