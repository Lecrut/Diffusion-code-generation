def feet_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    sample_feet = [1, 5, 10, 2.5, 3.75]
    result = feet_to_inches(sample_feet)
    print(result)