SQUARE_PROPERTIES = {
    'side': 5,
    'area_formula': lambda side: side ** 2
}

if __name__ == '__main__':
    side_length = SQUARE_PROPERTIES['side']
    area_of_square = SQUARE_PROPERTIES['area_formula'](side_length)
    print(f"The area of a square with side length {side_length} is {area_of_square}")