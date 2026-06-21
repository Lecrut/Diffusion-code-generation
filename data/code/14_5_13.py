def get_third_item(sequence):
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40]
    test_tuple = ("a", "b", "c", "d")
    print(get_third_item(test_list))
    print(get_third_item(test_tuple))