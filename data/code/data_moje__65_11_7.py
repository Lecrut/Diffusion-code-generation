def convert_feet_to_inches(foot_values):
    return [value * 12 for value in foot_values]

if __name__ == '__main__':
    sample_feet = [1, 2, 5.5, 10, 0.25]
    result = convert_feet_to_inches(sample_feet)
    print(result)