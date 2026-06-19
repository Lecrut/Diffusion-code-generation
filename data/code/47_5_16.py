def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("The given side lengths do not form a valid triangle.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        result1 = triangle_area(3, 4, 5)
        print(f"Area for sides 3, 4, 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = triangle_area(1, 2, 10)
        print(f"Area for sides 1, 2, 10: {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = triangle_area(7, 8, 9)
        print(f"Area for sides 7, 8, 9: {result3}")
    except ValueError as e:
        print(f"Error: {e}")