def square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    result = square_area(5)
    print(result)