def feet_to_inches(feet_values):
    return [foot * 12 for foot in feet_values]

if __name__ == '__main__':
    sample_feet = [1, 5, 10, 2.5]
    result = feet_to_inches(sample_feet)
    print(result)