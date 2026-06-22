def feet_to_inches(feet_values):
    return [value * 12 for value in feet_values]

if __name__ == '__main__':
    sample_feet = [1, 2, 5, 10, 15.5]
    result = feet_to_inches(sample_feet)
    print(result)