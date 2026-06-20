def get_first_last(seq):
    if seq:
        first = seq[0]
        last = seq[-1]
        return (first, last)
    else:
        return (None, None)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    empty_list = []
    empty_tuple = ()
    print(get_first_last(sample_list))
    print(get_first_last(sample_tuple))
    print(get_first_last(empty_list))
    print(get_first_last(empty_tuple))