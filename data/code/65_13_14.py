def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_values = [1.5, 10, 0.25, 0]
    for val in sample_values:
        result = feet_to_inches(val)
        print(result)