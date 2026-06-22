def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    test_list = [10, 20, 30]
    test_tuple = ("a", "b", "c")
    test_empty = []

    print(get_first_element(test_list))
    print(get_first_element(test_tuple))

    try:
        print(get_first_element(test_empty))
    except IndexError as e:
        print(e)