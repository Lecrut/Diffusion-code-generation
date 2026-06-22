def get_middle(seq):
    try:
        length = len(seq)
        if length == 0:
            raise IndexError("Sequence is empty")
        mid_index = (length - 1) // 2
        return seq[mid_index]
    except TypeError:
        raise TypeError("Input must be a sequence")

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    test_tuple = (10, 20, 30)
    test_string = "python"
    test_single = [42]
    test_empty = []

    print(get_middle(test_list))
    print(get_middle(test_tuple))
    print(get_middle(test_string))
    print(get_middle(test_single))
    try:
        get_middle(test_empty)
    except IndexError as e:
        print(f"Handled: {e}")