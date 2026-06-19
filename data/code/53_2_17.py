SQUARE_AREA_CONSTANT = 2

def get_side_length_and_area(side_length):
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_side_length1 = 3.5
    result1 = get_side_length_and_area(sample_side_length1)
    print(result1)

    sample_side_length2 = 7
    result2 = get_side_length_and_area(sample_side_length2)
    print(result2)