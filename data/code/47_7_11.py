def calculate_area(length, width):
    return length * width if length > 0 and width > 0 else None

if __name__ == '__main__':
    length = 9
    width = 2
    area = calculate_area(length, width)
    print(area)