def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_values = [1, 5.5, 0, 100, -3]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)