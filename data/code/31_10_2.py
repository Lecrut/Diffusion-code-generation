def square_of_side(side_length):
    squared_value = side_length * side_length
    return squared_value

if __name__ == '__main__':
    sample_side = 10
    computed_square = square_of_side(sample_side)
    print(computed_square)