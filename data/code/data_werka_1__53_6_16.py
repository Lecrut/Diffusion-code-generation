def calculate_square_area(side):
    if side < 0:
        raise ValueError('Side length cannot be negative')
    return side * side
if __name__ == '__main__':
    try:
        sample_side_1 = 4.0
        area_1 = calculate_square_area(sample_side_1)
        print(f'Side: {sample_side_1}, Area: {area_1}')
        sample_side_2 = 7.5
        area_2 = calculate_square_area(sample_side_2)
        print(f'Side: {sample_side_2}, Area: {area_2}')
        sample_side_3 = 0.0
        area_3 = calculate_square_area(sample_side_3)
        print(f'Side: {sample_side_3}, Area: {area_3}')
        invalid_side = -3.0
        area_4 = calculate_square_area(invalid_side)
        print(f'Side: {invalid_side}, Area: {area_4}')
    except ValueError as e:
        print(e)