def feet_to_inches(feet_list):
    return [feet * 12.0 for feet in feet_list]

if __name__ == '__main__':
    sample_feet = [1, 2.5, 5, 0, 10.125]
    result = feet_to_inches(sample_feet)
    print(result)