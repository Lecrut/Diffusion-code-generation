SIDE_LENGTH = 7

def calculate_area(side):
    half_side = side / 2
    perimeter = half_side * 4
    return perimeter * (side / 2)

if __name__ == '__main__':
    result = calculate_area(SIDE_LENGTH)
    print(result)