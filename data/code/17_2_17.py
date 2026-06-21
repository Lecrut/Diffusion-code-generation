def get_last_entry(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    iterator = iter(sequence)
    last = next(iterator)
    try:
        while True:
            last = next(iterator)
    except StopIteration:
        return last

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_last_entry(sample_tuple)
    print(result)