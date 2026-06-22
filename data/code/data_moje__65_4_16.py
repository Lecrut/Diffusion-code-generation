def feet_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    feet_values = [1, 2.5, 3, 0, 10]
    inches_values = feet_to_inches(feet_values)
    print(inches_values)