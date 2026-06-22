def repeat_tuple(base_tuple, count):
    return base_tuple * count

if __name__ == '__main__':
    sample_base_tuple = (1, 2, 3)
    sample_count = 5
    result = repeat_tuple(sample_base_tuple, sample_count)
    print(f"Base Tuple: {sample_base_tuple}, Count: {sample_count}")
    print("Result:")
    for item in result:
        print(item)