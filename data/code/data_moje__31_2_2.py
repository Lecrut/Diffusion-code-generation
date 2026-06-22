def square_area(side_length):
    if isinstance(side_length, int):
        return side_length * side_length
    else:
        return side_length ** 2

if __name__ == '__main__':
    print(square_area(5))
    print(square_area(3.5))
    print(square_area(0))
    print(square_area(10))