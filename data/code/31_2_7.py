def square_area(side):
    if isinstance(side, int):
        return side * side
    else:
        return side ** 2

if __name__ == '__main__':
    print(square_area(5))
    print(square_area(10))
    print(square_area(2.5))
    print(square_area(0))
    print(square_area(-3))