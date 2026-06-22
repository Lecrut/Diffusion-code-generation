KITE_SIDES = 2

def calculate_perimeter(side1, side2):
    return KITE_SIDES * (side1 + side2)

if __name__ == '__main__':
    perimeter = calculate_perimeter(5, 7)
    print(perimeter)