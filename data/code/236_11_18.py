def repeat_shape(shape, count):
    return shape * count

if __name__ == '__main__':
    sample_shape_list = ["A", "B"]
    sample_count = 3
    result1 = repeat_shape(sample_shape_list, sample_count)
    print(f"Shape: {sample_shape_list}, Count: {sample_count}")
    print("Result 1:")
    for row in result1:
        print(row)
    print("-" * 20)