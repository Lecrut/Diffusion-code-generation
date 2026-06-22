def area_of_square(side):
    if isinstance(side, (int, float)):
        return side * side
    else:
        raise ValueError("Invalid input type")

if __name__ == '__main__':
    print(area_of_square(5))
    print(area_of_square(3.5))