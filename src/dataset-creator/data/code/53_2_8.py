def count_from_start(sequence):
    if not hasattr(sequence, '__iter__'):
        raise TypeError(f"Expected an iterable object, got {type(sequence).__name__}")
    return len(list(sequence))
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    result_1 = count_from_start(sample_list)
    print(f"Count for list: {result_1}")
    try:
        invalid_input = None
        _ = count_from_start(invalid_input)
    except TypeError as e:
        print(f"Error handling test passed: {e}")
    result_2 = count_from_start(sample_tuple)
    print(f"Count for tuple: {result_2}")
    result_3 = count_from_start(sample_string)
    print(f"Count for string: {result_3}")