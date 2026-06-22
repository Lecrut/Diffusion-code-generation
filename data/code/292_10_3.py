def compute_rectangle_perimeter(side_a, side_b):
    perimeter = 2 * (side_a + side_b)
    return perimeter

if __name__ == '__main__':
    length = 10
    width = 7
    print(compute_rectangle_perimeter(length, width))