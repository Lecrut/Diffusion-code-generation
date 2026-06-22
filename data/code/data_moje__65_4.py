def convert_feet_to_inches(feet_list):
    return [f * 12 for f in feet_list]

if __name__ == '__main__':
    foot_values = [1, 2.5, 3, 10.75]
    inch_values = convert_feet_to_inches(foot_values)
    print(inch_values)