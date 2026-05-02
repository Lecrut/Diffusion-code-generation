import sys
def calculate_rectangle_area(length, width):
    return length * width
if __name__ == '__main__':
    length_sample = 10.5
    width_sample = 5.0
    area = calculate_rectangle_area(length_sample, width_sample)
    print(area)