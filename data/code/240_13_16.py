def compute_square_area(side_length):
    area = side_length ** 2
    return area

if __name__ == '__main__':
    sample_side = 7
    result = compute_square_area(sample_side)
    print(result)