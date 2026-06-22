def square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    side = 5
    result = square_area(side)
    print(result)