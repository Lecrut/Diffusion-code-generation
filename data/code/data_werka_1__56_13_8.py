def calculate_area(shape, side_length):
    if shape == 'square':
        return side_length ** 2
    elif shape == 'rectangle':
        return side_length * side_length
    else:
        raise ValueError('Unsupported shape')

def calculate_perimeter(shape, side_length):
    if shape == 'square':
        return 4 * side_length
    elif shape == 'rectangle':
        return 2 * (side_length + side_length)
    else:
        raise ValueError('Unsupported shape')

def compare_shapes(side_length):
    square_area = calculate_area('square', side_length)
    square_perimeter = calculate_perimeter('square', side_length)
    rectangle_area = calculate_area('rectangle', side_length)
    rectangle_perimeter = calculate_perimeter('rectangle', side_length)
    comparison_dict = {'square': {'area': square_area, 'perimeter': square_perimeter}, 'rectangle': {'area': rectangle_area, 'perimeter': rectangle_perimeter}}
    return comparison_dict
if __name__ == '__main__':
    side_length = 5
    result = compare_shapes(side_length)
    print(result)