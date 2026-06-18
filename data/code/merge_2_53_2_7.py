def count_from_start(sequence):
    try:
        return len(sequence)
    except TypeError:
        raise TypeError(f"Input must be iterable. Received {type(sequence).__name__}")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 'a', True)
    result_list = count_from_start(sample_list)
    result_tuple = count_from_start(sample_tuple)
    print(f"List count: {result_list}")
    print(f"Tuple count: {result_tuple}")