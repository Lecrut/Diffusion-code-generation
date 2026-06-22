def calculate_trapezoid_area(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Base lengths and height must be positive numbers")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    sample_base1 = 10
    sample_base2 = 20
    sample_height = 5
    result = calculate_trapezoid_area(sample_base1, sample_base2, sample_height)
    print(result)