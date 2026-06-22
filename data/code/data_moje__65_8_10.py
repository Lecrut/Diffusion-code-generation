FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    test_value = 12
    result = feet_to_inches(test_value)
    assert result == 144
    print(result)