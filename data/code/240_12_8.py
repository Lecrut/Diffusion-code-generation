def square_area(side):
    if isinstance(side, (int, float)):
        return side * side
    else:
        raise ValueError('Invalid input type. Please provide an integer or float.')
if __name__ == '__main__':
    print(square_area(5))
    print(square_area(3.5))