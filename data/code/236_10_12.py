SHAPE_COUNT = 3

def repeat_shape(shape, count):
    return [shape] * count

if __name__ == '__main__':
    sample_shape = "Square"
    repeated_shapes = repeat_shape(sample_shape, SHAPE_COUNT)
    print(repeated_shapes)