area_of_square = lambda side_length: side_length ** 2

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    for side in sample_sides:
        print(f"Area of square with side {side}: {area_of_square(side)}")