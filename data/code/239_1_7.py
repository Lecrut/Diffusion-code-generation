WIDTH = 10
HEIGHT = 5

def calculate_rectangle_perimeter(width=WIDTH, height=HEIGHT):
    return 2 * (width + height)

if __name__ == '__main__':
    perimeter = calculate_rectangle_perimeter()
    print(perimeter)