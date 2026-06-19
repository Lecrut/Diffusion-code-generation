def validate_input(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")

def calculate_area(base, height):
    try:
        validate_input(base, height)
        return 0.5 * base * height
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_area(sample_base, sample_height)
    print(area)