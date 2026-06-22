SHAPE_REPETITION_COUNT = 3

def repeat_shape(shape, count):
    return [shape] * count

if __name__ == '__main__':
    sample_shape = "Triangle"
    repeated_shapes = repeat_shape(sample_shape, SHAPE_REPETITION_COUNT)
    print(repeated_shapes)