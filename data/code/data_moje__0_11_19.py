CONVERSION_TABLE = {'meters_to_feet': 3.28084}

def meters_to_feet(length: float) -> float:
    factor = CONVERSION_TABLE['meters_to_feet']
    return length * factor

if __name__ == '__main__':
    sample_input = 10
    computed_result = meters_to_feet(sample_input)
    print(computed_result)