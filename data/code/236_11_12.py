TUPLE_REPETITION_LIMIT = 10 ** 6

def repeat_tuple(base_tuple, count):
    if not base_tuple:
        return ()
    if count <= 0:
        return ()
    repeated_tuple = base_tuple * count
    if len(repeated_tuple) > TUPLE_REPETITION_LIMIT:
        raise MemoryError('Repetition exceeds memory limit')
    return repeated_tuple
if __name__ == '__main__':
    sample_base_tuple = (1, 2, 3)
    sample_count = 5
    result = repeat_tuple(sample_base_tuple, sample_count)
    print(f'Base Tuple: {sample_base_tuple}, Count: {sample_count}')
    print('Result:')
    print(result)