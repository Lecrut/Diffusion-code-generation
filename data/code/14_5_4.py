def get_third_item(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c', 'd')
    print(get_third_item(sample_list))
    print(get_third_item(sample_tuple))
    try:
        print(get_third_item([1, 2]))
    except IndexError as e:
        print(e)