def get_third_element(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must contain at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    result_list = get_third_element(sample_list)
    result_tuple = get_third_element(sample_tuple)
    print(result_list)
    print(result_tuple)