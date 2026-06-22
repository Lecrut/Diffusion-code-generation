def get_perimeter(sides):
    if not all(side > 0 for side in sides):
        raise ValueError("Side lengths must be positive.")
    return sum(sides)

if __name__ == '__main__':
    try:
        print(get_perimeter((3, 4, 5)))
    except ValueError as e:
        print(e)
    try:
        print(get_perimeter((1, -2, 5)))
    except ValueError as e:
        print(e)