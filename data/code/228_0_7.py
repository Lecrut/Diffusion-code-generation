def print_equilateral_triangle(height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    try:
        print_equilateral_triangle(5)
    except ValueError as e:
        print(e)