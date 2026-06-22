def repeat_shape(shape, count):
    if not isinstance(shape, (str, int)) or not isinstance(count, int):
        raise ValueError("Shape must be a string or integer and count must be an integer")
    return [shape] * count

if __name__ == '__main__':
    sample_shape = "Triangle"
    sample_count = 4
    repeated_shapes = repeat_shape(sample_shape, sample_count)
    print(repeated_shapes)