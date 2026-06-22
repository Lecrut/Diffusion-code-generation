FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet: float) -> float:
    return feet * FEET_TO_INCHES_FACTOR

def feet_to_inches_batch(values: list) -> list:
    return [value * FEET_TO_INCHES_FACTOR for value in values]

if __name__ == '__main__':
    single_input = 10
    batch_input = [3, 7.5, 20]
    print(feet_to_inches(single_input))
    print(feet_to_inches_batch(batch_input))