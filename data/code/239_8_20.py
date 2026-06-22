def calculate_rectangle_perimeter(width: int, height: int) -> int:
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative integers")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        perimeter = calculate_rectangle_perimeter(5, 3)
        print(perimeter)
    except ValueError as e:
        print(e)