def feet_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    foot_measurements = [5.0, 10.5, 2, 15.3]
    inches_list = feet_to_inches(foot_measurements)
    print(inches_list)