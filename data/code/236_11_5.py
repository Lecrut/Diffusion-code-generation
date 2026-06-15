def repeat_shape(shape, count):
    if not shape:
        return []
    rows = len(shape)
    cols = len(shape[0])
    new_shape = []
    for _ in range(count):
        new_shape.extend(shape)
    return new_shape
if __name__ == '__main__':
    sample_shape_list = ["A", "B"]
    sample_count = 3
    result_list = repeat_shape(sample_shape_list, sample_count)
    print(result_list)
    sample_shape_2d = [
        ["X", "Y"],
        ["Z", "W"]
    ]
    sample_count_2d = 2
    result_2d = repeat_shape(sample_shape_2d, sample_count_2d)
    print(result_2d)