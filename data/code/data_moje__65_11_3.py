def convert_feet_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    sample_feet = [1.5, 2, 3.25, 5]
    result = convert_feet_to_inches(sample_feet)
    print(result)