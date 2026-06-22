def convert_feet_to_inches(foot_measurements):
    return [feet * 12 for feet in foot_measurements]

if __name__ == '__main__':
    sample_data = [1.0, 5.5, 10.25, 3.75, 0.5]
    result = convert_feet_to_inches(sample_data)
    print(result)