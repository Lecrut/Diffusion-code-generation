class ShapeRepeater:
    def __init__(self, shape):
        self.shape = shape

    def repeat(self, count):
        return [self.shape] * count

if __name__ == '__main__':
    sample_shape = "Square"
    sample_count = 4
    repeater = ShapeRepeater(sample_shape)
    repeated_shapes = repeater.repeat(sample_count)
    print(repeated_shapes)