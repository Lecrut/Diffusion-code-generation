CONVERSION_FACTOR = 12

def feet_to_inches(feet):
    unit_map = {"feet": 1, "inches": 12}
    factor = unit_map.get("inches", 1)
    return feet * (factor // unit_map.get("feet", 1))

if __name__ == '__main__':
    test_values = [0, 1, 10, 5.5, 100]
    for value in test_values:
        print(feet_to_inches(value))