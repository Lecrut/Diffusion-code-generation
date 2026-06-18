def get_first_element(sequence):
    return next(iter(sequence), None)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (50, 60)
    result_1 = get_first_element(sample_list)
    result_2 = get_first_element(sample_tuple)
    print(f"First element of list: {result_1}")
    print(f"First element of tuple: {result_2}")