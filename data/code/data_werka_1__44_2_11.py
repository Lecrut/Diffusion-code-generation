def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    L = 15
    W = 8
    try:
        perimeter = calculate_perimeter(L, W)
        print(perimeter)
    except ValueError as e:
        print(e)