def get_third_element(sequence):
    iterator = iter(sequence)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        raise IndexError("Sequence has fewer than three elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (100, 200, 300)
    result_list = get_third_element(sample_list)
    print(result_list)
    result_tuple = get_third_element(sample_tuple)
    print(result_tuple)