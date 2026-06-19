def first_element(sequence):
    return sequence[0] if sequence else None
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    empty_list = []
    empty_tuple = ()
    print(first_element(sample_list))
    print(first_element(sample_tuple))
    print(first_element(empty_list))
    print(first_element(empty_tuple))