def feet_to_inches(feet):
    inches_per_foot = 12
    total_inches = feet * inches_per_foot
    return total_inches

if __name__ == '__main__':
    sample_feet = 5
    result = feet_to_inches(sample_feet)
    print(result)
    sample_feet_float = 3.5
    result_float = feet_to_inches(sample_feet_float)
    print(result_float)