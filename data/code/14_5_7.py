def get_third_item(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three items")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    sample_string = "hello"
    print(get_third_item(sample_list))
    print(get_third_item(sample_tuple))
    print(get_third_item(sample_string))