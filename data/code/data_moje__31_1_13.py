def compute_square(side_length):
    squared_result = side_length * side_length
    return squared_result

if __name__ == '__main__':
    hardcoded_side = 7
    area_value = compute_square(hardcoded_side)
    print(area_value)