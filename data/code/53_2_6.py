def get_side_length_and_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    area = side_length * side_length
    return (side_length, area)
if __name__ == '__main__':
    try:
        result1 = get_side_length_and_area(5)
        print(result1)
        result2 = get_side_length_and_area(-3)
        print(result2)
    except ValueError as e:
        print(e)