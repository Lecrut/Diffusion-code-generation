def square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    result = square_area(5)
    print(result)
    result_negative = square_area(-5)
    print(result_negative)