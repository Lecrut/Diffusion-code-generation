def calculate_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    fixed_side_length = 3
    computed_area = calculate_area(fixed_side_length)
    print(computed_area)