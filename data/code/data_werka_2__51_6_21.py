class GeometryUtils:
    @staticmethod
    def calculate_perimeter(shape, *args):
        if shape == 'rectangle':
            if len(args) != 2:
                raise ValueError("Rectangle requires two arguments: length and width.")
            length, width = args
            return 2 * (length + width)
        elif shape == 'circle':
            if len(args) != 1:
                raise ValueError("Circle requires one argument: radius.")
            radius = args[0]
            return 2 * 3.14159 * radius
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 3)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)

    print("Rectangle Perimeter:", rectangle_perimeter)
    print("Circle Perimeter:", circle_perimeter)