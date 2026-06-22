class ShapeRepeater:
    def repeat_shape(self, shape, count):
        return [shape] * count

if __name__ == '__main__':
    repeater = ShapeRepeater()
    sample_shape = 'circle'
    sample_count = 5
    repeated_shapes = repeater.repeat_shape(sample_shape, sample_count)
    print(repeated_shapes)