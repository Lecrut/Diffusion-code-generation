def feet_to_inches(feet):
    inches_per_foot = 12
    total_inches = feet * inches_per_foot
    return total_inches

if __name__ == '__main__':
    sample_feet = 15
    result = feet_to_inches(sample_feet)
    print(result)