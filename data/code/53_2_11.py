def get_side_length_and_area(side_length):
    area = side_length * side_length
    return side_length, area

if __name__ == '__main__':
    sample_values = [3, 7.2, 10]
    for value in sample_values:
        side_length, area = get_side_length_and_area(value)
        print(f"Side Length: {side_length}, Area: {area}")