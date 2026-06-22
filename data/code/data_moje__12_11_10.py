def get_middle_element(seq):
    if not seq:
        raise ValueError("Sequence is empty")
    mid_index = len(seq) // 2
    return seq[mid_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(get_middle_element(sample_tuple))

    sample_tuple_2 = (10, 20, 30)
    print(get_middle_element(sample_tuple_2))

    sample_tuple_3 = (1, 2)
    print(get_middle_element(sample_tuple_3))

    sample_tuple_4 = ()
    try:
        get_middle_element(sample_tuple_4)
    except ValueError as e:
        print(e)