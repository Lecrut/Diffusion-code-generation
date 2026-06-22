def convert_feet_to_inches(feet):
    inches = feet * 12
    return inches

if __name__ == '__main__':
    feet_value = 5
    result = convert_feet_to_inches(feet_value)
    print(result)