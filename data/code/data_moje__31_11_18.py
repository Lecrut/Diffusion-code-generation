SQUARE_AREA_MULTIPLIER = {
    "square": 1
}

def get_square_area(side_length):
    unit_factor = SQUARE_AREA_MULTIPLIER.get("square", 0)
    return side_length * side_length * unit_factor

if __name__ == '__main__':
    result = get_square_area(15)
    print(result)