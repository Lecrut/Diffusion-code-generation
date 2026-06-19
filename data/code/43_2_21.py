def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        area1 = calculate_square_area(7)
        print(area1)
        area2 = calculate_square_area(3.5)
        print(area2)
        area3 = calculate_square_area('a')
        print(area3)
    except ValueError as e:
        print(e)