def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    test_values = [1, 5.5, 10, 0, 12.25]
    for value in test_values:
        result = feet_to_inches(value)
        print(result)