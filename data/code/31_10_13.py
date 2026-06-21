def compute_area_of_square(side):
    squared_result = side * side
    return squared_result

if __name__ == '__main__':
    test_side_length = 10
    calculated_area = compute_area_of_square(test_side_length)
    print(calculated_area)