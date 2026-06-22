CONVERSION_FACTOR = 12.0

def feet_to_inches(feet: float) -> float:
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    feet_value = 10
    inches_value = feet_to_inches(feet_value)
    print(inches_value)