LENGTH_TO_WIDTH_RATIO = 1.5

def calculate_area(length):
    width = length / LENGTH_TO_WIDTH_RATIO
    return length * width

if __name__ == '__main__':
    sample_length = 9
    area = calculate_area(sample_length)
    print(area)