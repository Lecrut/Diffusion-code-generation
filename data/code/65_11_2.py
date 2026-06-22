def feet_to_inches(feet_list):
    return [ft * 12 for ft in feet_list]

if __name__ == '__main__':
    sample_feet = [1, 2.5, 10, 0.5]
    inches = feet_to_inches(sample_feet)
    print(inches)