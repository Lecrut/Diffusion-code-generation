def feet_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    sample_feet = [1, 2.5, 5, 10.75]
    print(feet_to_inches(sample_feet))