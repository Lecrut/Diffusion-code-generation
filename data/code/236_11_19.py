def repeat_shape(base_tuple, count):
    return base_tuple * count

if __name__ == '__main__':
    sample_base_tuple = (1, 2)
    sample_count = 3
    result1 = repeat_shape(sample_base_tuple, sample_count)
    print(f"Base Tuple: {sample_base_tuple}, Count: {sample_count}")
    print("Result 1:")
    for item in result1:
        print(item)
    print("-" * 20)