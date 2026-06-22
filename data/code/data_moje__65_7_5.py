def feet_to_inches(feet):
    return feet * 36

if __name__ == '__main__':
    sample_values = [0, 1, 5.5, 100, -3]
    for val in sample_values:
        print(feet_to_inches(val))