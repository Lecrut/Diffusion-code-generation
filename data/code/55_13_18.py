def get_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    TRIANGLE_SIDES = (3, 4, 5)
    perimeter = get_perimeter(TRIANGLE_SIDES)
    print(perimeter)