def convert_feet_to_inches(feet_list):
    return [f * 12 for f in feet_list]

if __name__ == '__main__':
    feet_values = [1, 5, 10, 12.5]
    inches_values = convert_feet_to_inches(feet_values)
    print(inches_values)