CONVERSION_FACTOR = 2.54

def inches_to_centimeters(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Input must be a number")
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_inches = [10, 2.5, 7.2]
    for inch in sample_inches:
        print(f"{inch} inches is {inches_to_centimeters(inch)} centimeters")