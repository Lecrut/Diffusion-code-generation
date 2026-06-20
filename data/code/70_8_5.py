def check_sequence(seq):
    if seq:
        return (seq[0], seq[-1])
    else:
        return (None, None)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    empty_list = []
    empty_tuple = ()
    print(check_sequence(sample_list))
    print(check_sequence(sample_tuple))
    print(check_sequence(empty_list))
    print(check_sequence(empty_tuple))