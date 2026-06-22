SIDE_FACTOR = 1

def square_area(side_length):
    return side_length * SIDE_FACTOR * side_length

if __name__ == '__main__':
    test_values = [4, 7, 12]
    for val in test_values:
        print(square_area(val))