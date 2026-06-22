SIDE_LENGTH = 12

def get_area(side):
    squared_value = side * side
    return squared_value

if __name__ == '__main__':
    current_side = SIDE_LENGTH
    calculated_area = get_area(current_side)
    print(calculated_area)