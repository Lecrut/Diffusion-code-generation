def get_first_element(sequence):
    if not sequence:
        return None
    return sequence[0]

if __name__ == '__main__':
    sample_list = [25, 26, 27]
    sample_tuple = (28, 29, 30)
    empty_list = []
    empty_tuple = ()
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))