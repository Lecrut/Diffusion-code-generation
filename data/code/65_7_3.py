def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_feet_values = [0, 1, 5, 10.5, 100]
    for value in sample_feet_values:
        print(feet_to_inches(value))