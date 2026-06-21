def square_of_side(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be a number")
    return side_length * side_length

if __name__ == '__main__':
    side_value = 10
    area = square_of_side(side_value)
    print(area)