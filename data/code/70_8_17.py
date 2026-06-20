def fetch_sequence_ends(seq):
    if seq:
        first_item = seq[0]
        last_item = seq[-1]
        return (first_item, last_item)
    else:
        return (None, None)

if __name__ == '__main__':
    sample_string = "hello"
    sample_range = range(10)
    empty_set = set()
    
    print(fetch_sequence_ends(sample_string))
    print(fetch_sequence_ends(sample_range))
    print(fetch_sequence_ends(empty_set))