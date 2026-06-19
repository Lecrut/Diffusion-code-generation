LENGTH = 12
WIDTH = 6

def compute_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = compute_perimeter(LENGTH, WIDTH)
    print(perimeter)