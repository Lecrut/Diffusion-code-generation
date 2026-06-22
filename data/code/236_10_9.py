class ShapeRepeater:
    def __init__(self, shape):
        self.shape = shape

    def repeat(self, count):
        return [self.shape] * count

if __name__ == '__main__':
    repeater = ShapeRepeater("Circle")
    repeated_shapes = repeater.repeat(3)
    print(repeated_shapes)