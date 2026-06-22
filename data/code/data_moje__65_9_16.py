def convert_feet_to_inches(feet_value):
    inches_value = feet_value * 12
    return inches_value

if __name__ == '__main__':
    input_feet = 5
    result = convert_feet_to_inches(input_feet)
    print(result)