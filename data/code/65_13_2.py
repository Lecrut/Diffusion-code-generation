def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_values = [1, 5.5, 10, 0.25, 100]
    for value in sample_values:
        print(feet_to_inches(value))