def convert_feet_to_inches(foot_measurements):
    return [measurement * 12.0 for measurement in foot_measurements]

if __name__ == '__main__':
    sample_measurements = [1.0, 5.5, 10.25, 0.5, 12.0]
    result = convert_feet_to_inches(sample_measurements)
    print(result)