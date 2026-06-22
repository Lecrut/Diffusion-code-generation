def convert_feet_to_inches(foot_values):
    return [feet * 12 for feet in foot_values]

if __name__ == '__main__':
    feet_list = [1.5, 2.0, 3.25, 10.0]
    inches_list = convert_feet_to_inches(feet_list)
    print(inches_list)