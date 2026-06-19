def calculate_square_side_length(area):
    return area ** 0.5

if __name__ == '__main__':
    area_value = 25.0
    side_length = calculate_square_side_length(area_value)
    print(side_length)