def count_from_start(sequence):
    try:
        return len(sequence)
    except TypeError:
        raise TypeError(f"Expected an iterable input but received {type(sequence).__name__}.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    result_1 = count_from_start(sample_list)
    print(f"Count from start for list: {result_1}")
    result_2 = count_from_start(sample_tuple)
    print(f"Count from start for tuple: {result_2}")