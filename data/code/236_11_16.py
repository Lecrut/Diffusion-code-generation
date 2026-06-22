MAX_REPETITION_COUNT = 1000

def repeat_shape(base_tuple, count):
    if not base_tuple or count <= 0:
        return ()
    repeated_list = base_tuple * count
    return tuple(repeated_list)
if __name__ == '__main__':
    sample_base_tuple = (1, 2, 3)
    sample_count = 5
    result1 = repeat_shape(sample_base_tuple, sample_count)
    print(f'Base Tuple: {sample_base_tuple}, Count: {sample_count}')
    print('Result 1:', result1)