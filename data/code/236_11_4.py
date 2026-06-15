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
    result1 = repeat_shape(sample_shape_list, sample_count)
    print(f"Shape: {sample_shape_list}, Count: {sample_count}")
    print(f"Result (List of Lists): {result1}")
    sample_shape_2d = [
        ["X", "Y"],
        ["Z", "W"]
    ]
    sample_count_2 = 2
    result2 = repeat_shape(sample_shape_2d, sample_count_2)
    print(f"\nShape: {sample_shape_2d}, Count: {sample_count_2}")
    print(f"Result (List of Lists): {result2}")