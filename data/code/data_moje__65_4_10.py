def feet_to_inches(feet_values):
    return [feet * 12 for feet in feet_values]

if __name__ == '__main__':
    sample_feet = [1, 2.5, 3, 4.75, 5]
    print(feet_to_inches(sample_feet))