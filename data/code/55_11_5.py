def calculate_triangle_perimeter(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        raise ValueError("All sides must be positive numbers")
if __name__ == '__main__':
    a_val = 3
    b_val = 4
    c_val = 5
    try:
        perimeter = calculate_triangle_perimeter(a_val, b_val, c_val)
        print(perimeter)
    except ValueError as e:
        print(e)
    a_val_invalid = -1
    b_val_invalid = 4
    c_val_invalid = 5
    try:
        perimeter_invalid = calculate_triangle_perimeter(a_val_invalid, b_val_invalid, c_val_invalid)
        print(perimeter_invalid)
    except ValueError as e:
        print(e)