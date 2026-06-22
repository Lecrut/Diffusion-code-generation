def feet_to_inches(foot_measurements):
    return [measure * 12 for measure in foot_measurements]

if __name__ == '__main__':
    sample_feet = [5, 5.5, 6, 6.25, 7]
    inches = feet_to_inches(sample_feet)
    print(inches)