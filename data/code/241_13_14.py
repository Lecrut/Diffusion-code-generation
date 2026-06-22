def calculate_area(length, width):
    area = length * width
    return area

if __name__ == '__main__':
    sample_length = 7
    sample_width = 4
    computed_area = calculate_area(sample_length, sample_width)
    print(computed_area)