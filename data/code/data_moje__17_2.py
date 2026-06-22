def get_last_entry(sequence):
    iterator = iter(sequence)
    last = None
    while True:
        try:
            last = next(iterator)
        except StopIteration:
            break
    return last

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_last_entry(sample_tuple)
    print(result)