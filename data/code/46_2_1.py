def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    sides = [3.0, 4.0, 5.0]
    result = calculate_perimeter(sides[0], sides[1], sides[2])
    print(result)