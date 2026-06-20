def get_sequence_ends(seq):
    if seq:
        first = seq[0]
        last = seq[-1]
        return (first, last)
    else:
        return (None, None)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    
    print(get_sequence_ends(sample_list))
    print(get_sequence_ends(sample_tuple))
    print(get_sequence_ends(empty_list))
    print(get_sequence_ends(empty_tuple))