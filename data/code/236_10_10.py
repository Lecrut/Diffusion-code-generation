def repeat_shape(shape, count):
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    return [shape] * count

if __name__ == '__main__':
    sample_shape = "Circle"
    sample_count = 3
    repeated_shapes = repeat_shape(sample_shape, sample_count)
    print(repeated_shapes)