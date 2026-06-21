def square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_side = 5
    result = square_area(sample_side)
    print(result)