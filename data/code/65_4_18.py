def convert_feet_to_inches(foot_values):
    return [feet * 12 for feet in foot_values]

if __name__ == '__main__':
    foot_values = [1, 2.5, 10, 0.5]
    inch_values = convert_feet_to_inches(foot_values)
    print(inch_values)