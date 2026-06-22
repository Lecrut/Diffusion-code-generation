def repeat_shape(shape, count):
    return [shape] * count

if __name__ == '__main__':
    sample_shape = "Triangle"
    sample_count = 4
    repeated_shapes = repeat_shape(sample_shape, sample_count)
    print(repeated_shapes)