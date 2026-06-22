FEET_TO_INCHES_FACTOR = 12

def convert_feet_to_inches(feet: float) -> float:
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_feet = 5
    result_inches = convert_feet_to_inches(sample_feet)
    print(result_inches)