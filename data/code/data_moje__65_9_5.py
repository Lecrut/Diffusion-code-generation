def convert_feet_to_inches(feet):
    inches = feet * 12
    return inches

if __name__ == '__main__':
    value_in_feet = 5
    result = convert_feet_to_inches(value_in_feet)
    print(result)