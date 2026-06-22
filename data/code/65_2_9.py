def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_values = [0, 1, 2.5, 10, -5]
    for value in sample_values:
        print(feet_to_inches(value))