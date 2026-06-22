def convert_feet_to_inches(feet_value):
    inches_per_foot = 12
    total_inches = feet_value * inches_per_foot
    return total_inches

if __name__ == '__main__':
    sample_feet = 5
    result_in_inches = convert_feet_to_inches(sample_feet)
    print(result_in_inches)