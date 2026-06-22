LENGTH = 10
WIDTH = 5

def calculate_perimeter(length, width):
    return 2 * (length + width)
if __name__ == '__main__':
    perimeter_result = calculate_perimeter(LENGTH, WIDTH)
    print(perimeter_result)