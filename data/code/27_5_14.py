def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))