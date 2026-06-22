def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type")
    return feet * 12

if __name__ == '__main__':
    result = feet_to_inches(5.5)
    print(result)
    result2 = feet_to_inches(10)
    print(result2)