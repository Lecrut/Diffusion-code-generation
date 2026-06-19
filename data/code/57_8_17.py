import math

def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 10
        sample_height = 5
        result = calculate_area(sample_base, sample_height)
        print(result)
    except Exception as e:
        print(e)