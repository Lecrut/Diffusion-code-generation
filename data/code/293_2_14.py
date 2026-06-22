class GeometryCalculator:

    @staticmethod
    def area(shape_type, *args):
        if shape_type == 'circle':
            radius = args[0]
            return math.pi * radius ** 2
        elif shape_type == 'square':
            side_length = args[0]
            return side_length ** 2
        elif shape_type == 'rectangle':
            length, width = args
            return length * width
        else:
            raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    print(GeometryCalculator.area('circle', 5))
    print(GeometryCalculator.area('square', 4))
    print(GeometryCalculator.area('rectangle', 3, 2))