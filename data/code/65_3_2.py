def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_values = [1, 2.5, 0, 10, 5.75]
    for val in sample_values:
        result = feet_to_inches(val)
        print(result)