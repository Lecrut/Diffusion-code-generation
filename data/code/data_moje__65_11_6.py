def convert_feet_to_inches(foot_measurements):
    return [foot * 12 for foot in foot_measurements]

if __name__ == '__main__':
    sample_feet = [1.5, 2.0, 3.25, 5.0, 7.5]
    inches = convert_feet_to_inches(sample_feet)
    print(inches)