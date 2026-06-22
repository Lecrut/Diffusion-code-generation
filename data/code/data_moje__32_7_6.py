def multiply_dimensions(a, b):
    return a * b

def validate_dimensions(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if a < 0 or b < 0:
        raise ValueError("Dimensions must be non-negative")

def calculate_rectangle_area(length, width):
    validate_dimensions(length, width)
    return multiply_dimensions(length, width)

if __name__ == '__main__':
    len1 = 7
    wid1 = 4.25
    len2 = 10
    wid2 = 10
    result1 = calculate_rectangle_area(len1, wid1)
    result2 = calculate_rectangle_area(len2, wid2)
    print(result1)
    print(result2)