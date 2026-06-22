def feet_to_inches(feet_list):
    return [f * 12 for f in feet_list]

if __name__ == '__main__':
    feet_values = [1.5, 3, 6, 10.25]
    inches = feet_to_inches(feet_values)
    print(inches)