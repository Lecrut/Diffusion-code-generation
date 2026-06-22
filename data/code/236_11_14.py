def repeat_shape(shape, count):
    if not shape:
        return []
    repeated_shape = [item for _ in range(count) for item in shape]
    return repeated_shape

if __name__ == '__main__':
    sample_shape_list = ["A", "B"]
    sample_count = 3
    result1 = repeat_shape(sample_shape_list, sample_count)
    print(f"Shape: {sample_shape_list}, Count: {sample_count}")
    print("Result 1:")
    for item in result1:
        print(item)
    print("-" * 20)