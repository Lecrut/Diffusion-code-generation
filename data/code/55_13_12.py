def get_perimeter(sides):
    a, b, c = sides
    if any(x <= 0 for x in sides):
        raise ValueError("Side lengths must be positive.")
    return a + b + c

if __name__ == '__main__':
    try:
        print(get_perimeter((3, 4, 5)))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(get_perimeter((1, 2, 3)))
    except ValueError as e:
        print(f"Error: {e}")