def convert_feet_to_inches(foot_measurements):
    return [measurement * 12 for measurement in foot_measurements]

if __name__ == '__main__':
    sample_feet = [1.5, 5, 10.75, 0.25, 3]
    result = convert_feet_to_inches(sample_feet)
    print(result)