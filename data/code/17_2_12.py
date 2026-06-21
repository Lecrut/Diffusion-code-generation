def get_last_entry(seq):
    last = None
    for item in seq:
        last = item
    return last

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_last_entry(sample_tuple)
    print(result)