def check_first_last(sequence):
    if sequence:
        return (sequence[0], sequence[-1])
    else:
        return (None, None)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    empty_list = []
    empty_tuple = ()
    print(check_first_last(sample_list))
    print(check_first_last(sample_tuple))
    print(check_first_last(empty_list))
    print(check_first_last(empty_tuple))