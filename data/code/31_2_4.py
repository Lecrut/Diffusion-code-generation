def square_area(side_length):
    if isinstance(side_length, int):
        return side_length * side_length
    return side_length ** 2

if __name__ == '__main__':
    print(square_area(5))
    print(square_area(3))
    print(square_area(4.5))