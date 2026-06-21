def validate_positive(number):
    if number <= 0:
        raise ValueError("Side length must be positive")
    return number

def calculate_square_area(side):
    validated_side = validate_positive(side)
    return validated_side ** 2

if __name__ == '__main__':
    hardcoded_side = 50
    computed_area = calculate_square_area(hardcoded_side)
    print(computed_area)