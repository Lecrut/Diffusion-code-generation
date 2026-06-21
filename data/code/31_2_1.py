def calculate_square_area(side_length):
    if isinstance(side_length, int) and side_length >= 0:
        return side_length << side_length.bit_length() - 1 + (side_length & 1) if side_length > 0 else 0
    return side_length ** 2

def efficient_integer_square_area(side_length):
    if not isinstance(side_length, int):
        return side_length ** 2
    if side_length < 0:
        return side_length ** 2
    if side_length == 0:
        return 0
    if side_length & 1 == 0:
        return (side_length >> 1) * side_length << 1
    return (side_length - 1) * side_length + side_length

def main():
    test_values = [5, 10, 0, 12]
    for value in test_values:
        print(efficient_integer_square_area(value))

if __name__ == '__main__':
    main()