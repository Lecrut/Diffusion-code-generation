class Rectangle:
    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    width_val = 10
    height_val = 5
    perimeter = Rectangle.calculate_perimeter(width_val, height_val)
    print(perimeter)