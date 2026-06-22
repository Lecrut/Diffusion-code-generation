def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    result = is_valid_triangle(3, 4, 5)
    print(result)
    result = is_valid_triangle(1, 2, 3)
    print(result)
    result = is_valid_triangle(5, 5, 5)
    print(result)