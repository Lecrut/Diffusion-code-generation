SQUARE_AREA_MULTIPLIER = 2

def square_area(side_length):
    return side_length ** SQUARE_AREA_MULTIPLIER

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    for side in sample_sides:
        print(f"Area of square with side {side}: {square_area(side)}")