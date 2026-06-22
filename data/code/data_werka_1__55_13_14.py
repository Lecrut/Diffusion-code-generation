TRIANGLE_SIDES = 3

def get_perimeter(sides):
    if len(sides) != TRIANGLE_SIDES:
        raise ValueError("Exactly three side lengths are required.")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    sides1 = (3, 4, 5)
    try:
        print(get_perimeter(sides1))
    except ValueError as e:
        print(e)

    sides2 = (7, 8, 9)
    try:
        print(get_perimeter(sides2))
    except ValueError as e:
        print(e)