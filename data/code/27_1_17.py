def is_valid_triangle(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sides_1 = 3.0
    sides_2 = 4.0
    sides_3 = 5.0
    sides_4 = 1.0
    sides_5 = 2.0
    sides_6 = 10.0
    print(is_valid_triangle(sides_1, sides_2, sides_3))
    print(is_valid_triangle(sides_4, sides_5, sides_6))