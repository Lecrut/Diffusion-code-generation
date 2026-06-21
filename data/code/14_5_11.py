def get_third_item(sequence):
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_item(sample_list))

    sample_tuple = ('a', 'b', 'c', 'd')
    print(get_third_item(sample_tuple))

    sample_string = "hello"
    print(get_third_item(sample_string))