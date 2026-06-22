def repeat_shape(base_tuple, count):
    if not base_tuple:
        return ()
    return base_tuple * count

if __name__ == '__main__':
    sample_tuple = ("A", "B")
    sample_count = 3
    result1 = repeat_shape(sample_tuple, sample_count)
    print(f"Tuple: {sample_tuple}, Count: {sample_count}")
    print("Result:")
    for item in result1:
        print(item)