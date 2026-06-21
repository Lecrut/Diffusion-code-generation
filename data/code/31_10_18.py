def calculate_side_square(side_length):
    squared_result = side_length * side_length
    return squared_result

if __name__ == '__main__':
    side_length_value = 10
    computed_value = calculate_side_square(side_length_value)
    print(computed_value)