def calculate_square_side_length(area):
    side_length = area ** 0.5
    return side_length

if __name__ == '__main__':
    area_value = 25.0
    side_length = calculate_square_side_length(area_value)
    print(side_length)