UNIT_CONVERSION_RATES = {
    'feet_to_inches': 12
}

def feet_to_inches(feet):
    rate = UNIT_CONVERSION_RATES['feet_to_inches']
    return feet * rate

if __name__ == '__main__':
    test_values = [3, 6.25, 0, -1]
    for val in test_values:
        result = feet_to_inches(val)
        print(result)