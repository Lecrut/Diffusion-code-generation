def create_repeated_tuples(base_tuple, count):
    if not base_tuple:
        return ()
    repeated_tuples = (base_tuple,) * count
    return repeated_tuples

if __name__ == '__main__':
    sample_base_tuple = ('X', 'Y')
    sample_count = 5
    result1 = create_repeated_tuples(sample_base_tuple, sample_count)
    print(f"Base Tuple: {sample_base_tuple}, Count: {sample_count}")
    print("Result:")
    for t in result1:
        print(t)