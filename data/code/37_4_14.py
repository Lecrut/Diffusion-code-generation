def get_parallelogram_area(base, height):
    product = base * height
    return product

if __name__ == '__main__':
    side_length = 12.75
    perpendicular_height = 4.2
    calculated_area = get_parallelogram_area(side_length, perpendicular_height)
    print(calculated_area)