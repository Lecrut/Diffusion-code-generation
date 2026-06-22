def convert_feet_to_inches(feet):
    inches_per_foot = 12
    total_inches = feet * inches_per_foot
    return total_inches

if __name__ == '__main__':
    sample_feet_values = [1, 2.5, 5, 10]
    for feet_value in sample_feet_values:
        result = convert_feet_to_inches(feet_value)
        print(result)