def calculate_trapezoid_area(base_a, base_b, height):
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative")
    return (base_a + base_b) * height / 2

if __name__ == '__main__':
    base_1 = 10
    base_2 = 20
    h = 5
    result = calculate_trapezoid_area(base_1, base_2, h)
    print(result)