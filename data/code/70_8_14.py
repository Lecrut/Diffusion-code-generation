def first_last(seq):
    if not seq:
        return (None, None)
    return (seq[0], seq[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    print(first_last(sample_list))
    print(first_last(sample_tuple))
    print(first_last(empty_list))
    print(first_last(empty_tuple))