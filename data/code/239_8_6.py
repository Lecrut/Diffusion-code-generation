def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    parameters = {
        'width': 5,
        'height': 3
    }
    perimeter = calculate_rectangle_perimeter(**parameters)
    print(perimeter)