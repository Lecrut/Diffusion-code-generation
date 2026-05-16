def get_side_length_and_area(side_length):
    area = side_length * side_length
    return (side_length, area)
if __name__ == '__main__':
    sample_side = 5
    result = get_side_length_and_area(sample_side)
    print(result)