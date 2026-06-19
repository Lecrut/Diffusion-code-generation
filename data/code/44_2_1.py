def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    L = 15
    W = 8
    perimeter = calculate_perimeter(L, W)
    print(perimeter)